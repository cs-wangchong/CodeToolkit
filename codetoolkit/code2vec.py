#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path
import pickle
import math
import time
import multiprocessing
import itertools
from collections import defaultdict
import logging
import traceback
import re

import numpy as np
from gensim.models import FastText

from .javalang.parse import parse
from .javalang.tree import *
from .javalang.tokenizer import Identifier
from .delimiter import Delimiter

MIN_IDENTIFIER = 5
MAX_IDENTIFIER = 200
MAX_DISTANCE = 20
SEQUENCE_LEN = 50
SEQ_PER_START = 2

MIN_WORD_COUNT = 10

def _build_identifier_graph(tree):
    ## solve member reference and method invocation
    identifiers = set(token.value for token in tree.tokens(Identifier))
    normalized_idens = set(Delimiter.split_camel(iden, to_lower=True).replace(" ", "_") for iden in identifiers)
    # print(normalized_idens)
    if not (MIN_IDENTIFIER <= len(normalized_idens) <= MAX_IDENTIFIER):
        return dict()
    graph = dict()
    paths = list()
    for path, ast_node in tree:
        for child in ast_node.children:
            if not (isinstance(child, str) and child in identifiers):
                continue
            path += (Delimiter.split_camel(child, to_lower=True).replace(" ", "_"), )
            paths.append(path)
    for path1, path2 in itertools.combinations(paths, 2):
        iden1, iden2 = path1[-1], path2[-1]
        if iden1 == iden2:
            continue
        offset = max(max(len(path1), len(path2)) - MAX_DISTANCE, 0)
        index = 0
        for i, (ele1, ele2) in enumerate(zip(path1[offset:], path2[offset:])):
            if ele1 is not ele2:
                index = i
                break
        dis = len(path1[index:]) + len(path2[index:])
        if dis > MAX_DISTANCE:
            continue
        if (iden1, iden2) in graph and dis >= graph[iden1, iden2]:
            continue
        graph[iden1, iden2] = dis
        graph[iden2, iden1] = dis
    return graph

def _random_walk(graph):
    transition_table = defaultdict(list)
    for (u, v), dis in graph.items():
        transition_table[u].append((v, dis))
    # print(transition_table)
    for u, out_edges in list(transition_table.items()):
        neighbours, distances = zip(*out_edges)
        total_dis = sum(distances)
        weights = [math.log2(total_dis / dis) for dis in distances]
        total_weight = sum(weights)
        probs = [w / total_weight if total_weight > 0 else 1. for w in weights]
        transition_table[u] = neighbours, probs
    # print(transition_table)

    iden_seqs = list()    
    for identifier in transition_table:
        for _ in range(SEQ_PER_START):
            seq = list()
            hop = 0
            cur_identifier = identifier
            while hop < SEQUENCE_LEN:
                # seq.extend(slicer.slice(cur_identifier))
                seq.append(cur_identifier)
                neighbours, probs = transition_table[identifier]
                cur_identifier = np.random.choice(neighbours, 1, probs)[0]
                hop += 1
            iden_seqs.append(seq)
    return iden_seqs

def _extract_for_subtree(tree):
    graph = _build_identifier_graph(tree)
    iden_seqs = _random_walk(graph)
    return iden_seqs

def _extract_for_code(code, level="method"):
    try:
        ast = parse(code)
    except:
        # logging.error("parse code error")
        return set(), defaultdict(int)
    subtrees = [md for _, md in ast.filter((MethodDeclaration, ConstructorDeclaration))] if level == "method" else [ast]
    if len(subtrees) == 0:
        return set(), defaultdict(int)

    iden_seqs = list()
    word2count = defaultdict(int)
    for tree in subtrees:
        words = set()
        for seq in _extract_for_subtree(tree):
            delimited_seq = []
            for iden in seq:
                iden = Delimiter.split_camel(iden, to_lower=True).replace(" ", "_")
                delimited_seq.append(iden)
                for word in iden.split("_"):
                    words.add(word)
            iden_seqs.append(delimited_seq)
        for word in words:
            word2count[word] = word2count[word] + 1
        
    return iden_seqs, word2count

def generate_corpus(input_file, sequence_file, meta_file, buf_size=1000):
    with Path(input_file).open("rb") as f:
        codes = pickle.load(f)
    # print("finish loading code.")
    try:
        beg_time = time.time()
        seqs = list()
        word2count = defaultdict(int)
        seq_f = Path(sequence_file).open("w", encoding="utf-8")
        seq_num = 0
        num = 0
        for pid, cid, code in codes:
            num += 1
            _seqs, _word2count = _extract_for_code(code)
            seqs.extend(_seqs)
            for word, count in _word2count.items():
                word2count[word] = word2count[word] + count 
            if num % buf_size == 0 or num == len(codes):
                logging.info(f"processed code: {num}/{len(codes)}, vocab size: {len(word2count)}, cost time: {time.time() - beg_time}s.")
                seq_f.write("\n".join([" ".join(seq) for seq in seqs]))
                seq_f.flush()
                seq_num += len(seqs)
                seqs.clear()
            # if len(_seqs) == 0:
            #     print(code)
            # break
        seq_f.close()
        with Path(meta_file).open("wb") as f:
            pickle.dump((seq_num, word2count), f)
    except:
        traceback.print_exc()

def train(corpus_files, meta_files, emb_path, workers=32):
    word2count = defaultdict(int)
    seq_num = 0
    for meta_file in meta_files:
        with Path(meta_file).open("rb") as f:
            _seq_num, _word2count = pickle.load(f)
        seq_num += _seq_num
        for word, count in _word2count.items():
            word2count[word] = word2count[word] + count

    class Corpus:
        def __init__(self, fnames):
            self.fnames = fnames
    
        def __iter__(self):
            for fname in self.fnames:
                with Path(fname).open("r", encoding="utf-8") as f:
                    sentences = f.readlines()
                    for sent in sentences:
                        yield re.split(r"\s_", sent.strip())

    fasttext = FastText(sg=1, hs=1, vector_size=100, window=10, min_count=MIN_WORD_COUNT, workers=workers)
    fasttext.build_vocab_from_freq(word2count)
    fasttext.train(Corpus(corpus_files), total_examples=seq_num, epochs=5)
    fasttext.wv.save(emb_path)
    logging.info(f"vocab size: {len(fasttext.wv.key_to_index)}")
    