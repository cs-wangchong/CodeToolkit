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
from gensim.models import FastText, Word2Vec

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

IGNORE_NODES = (Annotation, )

def _build_identifier_graph(tree):
    ## solve member reference and method invocation
    identifiers = set(token.value for token in tree.tokens(Identifier))
    normalized_idens = set(Delimiter.split_camel(iden, to_lower=True).replace(" ", "_") for iden in identifiers)
    # print(normalized_idens)
    if not (MIN_IDENTIFIER <= len(normalized_idens) <= MAX_IDENTIFIER):
        return dict()
    leaf2ancestors = defaultdict(dict)
    for path, ast_node in tree:
        if isinstance(ast_node, IGNORE_NODES):
            continue
        path = (ast_node, ) + tuple(n for n in reversed(path) if isinstance(n, Node))
        path = path[:MAX_DISTANCE]
        for child in ast_node.children:
            if not (isinstance(child, str) and child in identifiers):
                continue
            leaf = Delimiter.split_camel(child, to_lower=True).replace(" ", "_")
            for dis, ancestor in enumerate(path, start=1):
                if ancestor in leaf2ancestors[leaf] and leaf2ancestors[leaf][ancestor] < dis:
                    continue
                leaf2ancestors[leaf][ancestor] = dis
            
    graph = dict()
    for leaf1, leaf2 in itertools.combinations(leaf2ancestors.keys(), 2):
        ancestors1, ancestors2 = leaf2ancestors[leaf1], leaf2ancestors[leaf2]
        common_ancestors = set(ancestors1.keys()) & set(ancestors2.keys())
        if len(common_ancestors) == 0:
            continue
        dis = min(ancestors1[common_anc] + ancestors2[common_anc] for common_anc in common_ancestors)
        if dis > MAX_DISTANCE:
            continue
        graph[leaf1, leaf2] = dis
        graph[leaf2, leaf1] = dis
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

    iden_seqs = list()   
    seq_len = min(len(transition_table), SEQUENCE_LEN) 
    for identifier in transition_table:
        for _ in range(SEQ_PER_START):
            seq = list()
            hop = 0
            cur_identifier = identifier
            while hop < seq_len:
                # seq.extend(slicer.slice(cur_identifier))
                seq.append(cur_identifier)
                neighbours, probs = transition_table[cur_identifier]
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
        return set(), defaultdict(int)
    subtrees = [md for _, md in ast.filter((MethodDeclaration, ConstructorDeclaration))] if level == "method" else [ast]
    if len(subtrees) == 0:
        return set(), defaultdict(int)

    iden_seqs = list()
    word2count = defaultdict(int)
    for tree in subtrees:
        words = set()
        for seq in _extract_for_subtree(tree):
            # print(seq)
            delimited_seq = []
            for iden in seq:
                delimited_seq.append(iden)
                for word in iden.split("_"):
                    word2count[word] = word2count[word] + 1
            iden_seqs.append(delimited_seq)
        for word in words:
            word2count[word] = word2count[word] + 1      
    return iden_seqs, word2count

def generate_corpus(input_file, sequence_file, meta_file, level="method", buf_size=1000):
    with Path(input_file).open("rb") as f:
        codes = pickle.load(f)
    # print("finish loading code.")
    
    beg_time = time.time()
    seqs = list()
    word2count = defaultdict(int)
    seq_f = Path(sequence_file).open("w", encoding="utf-8")
    seq_num = 0
    num = 0
    for pid, cid, code in codes:
        num += 1
        try:
            _seqs, _word2count = _extract_for_code(code, level=level)
        except:
            logging.error(traceback.format_exc())
            continue
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
    

def train(corpus_files, meta_files, model_path=None, emb_path=None, model="fasttext", vector_size=100, window=15, min_count=MIN_WORD_COUNT, epochs=5, workers=32, fine_tuning=False):
    word2count = defaultdict(int)
    seq_num = 0
    for meta_file in meta_files:
        with Path(meta_file).open("rb") as f:
            _seq_num, _word2count = pickle.load(f)
        seq_num += _seq_num
        for word, count in _word2count.items():
            word2count[word] = word2count[word] + count
    logging.info(f"total examples: {seq_num}")

    class Corpus:
        def __init__(self, fnames):
            self.fnames = fnames
    
        def __iter__(self):
            for fname in self.fnames:
                with Path(fname).open("r", encoding="utf-8") as f:
                    sentences = f.readlines()
                    for sent in sentences:
                        yield re.split(r"[\s_]", sent.strip())
    
    model_cls = FastText if model == "fasttext" else Word2Vec
    if fine_tuning and model_path:
        model = model_cls.load(model_path)
    else:
        model = model_cls(sg=1, hs=1, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
        model.build_vocab_from_freq(word2count)
    model.train(Corpus(corpus_files), total_examples=seq_num, epochs=epochs)
    if model_path:
        model.save(model_path)
    if emb_path:
        model.wv.save(emb_path)
    logging.info(f"vocab size: {len(model.wv.key_to_index)}")
    