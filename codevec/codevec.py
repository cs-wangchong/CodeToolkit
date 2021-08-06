#!/usr/bin/env python
# -*- encoding: utf-8 -*-



from os import curdir
from pathlib import Path
import pickle
import math
import multiprocessing
import logging
import time
import random
import numpy as np
import itertools
from collections import defaultdict

from gensim.models import Word2Vec
import networkx as nx

from javalang.parse import parse
from javalang.tree import *
from javalang.ast import Node
from javalang.tokenizer import Identifier


PROCESSOR_NUM = 32
MAX_IDENTIFIER = 200
MAX_DIS = 20
MAX_SEQ_LEN = 50
NUM_SEQ = 2

MIN_WORD_COUNT = 1


def generate_sequences(input_file, output_file):
    with Path(input_file).open("rb") as f:
        codes = pickle.load(f)
    seqs = list()
    all_identifiers = set()
    f = Path(output_file).open("w", encoding="utf-8")
    for pid, cid, code in codes:
        try:
            ast = parse(code)
        except:
            print("parse code error")
            continue
        identifiers = set(token.value for token in ast.tokens() if isinstance(token, Identifier))
        if len(identifiers) > MAX_IDENTIFIER:
            continue
        all_identifiers.update(identifiers)
        graph = convert_ast_to_graph(ast, identifiers)
        seqs.extend(random_walk(graph))
        if len(seqs) >= 10000:
            all_identifiers = list(all_identifiers)
            iden2chunks = {iden: ["_".join(chunk.split()) for chunk in chunks] for iden, chunks in zip(all_identifiers, slicer.slice(*[Delimiter.split_camel_strict(identifier) for identifier in all_identifiers])[0])}
            _seqs = []
            for seq in seqs:
                _seq = []
                for iden in seq:
                    _seq.extend(iden2chunks[iden])
                _seqs.append(_seq)
            f.write("\n".join([" ".join(seq) for seq in _seqs]))
            seqs.clear()
            all_identifiers = set()
    all_identifiers = list(all_identifiers)
    iden2chunks = {iden: ["_".join(chunk.split()) for chunk in chunks] for iden, chunks in zip(all_identifiers, slicer.slice(*[Delimiter.split_camel_strict(identifier) for identifier in all_identifiers])[0])}
    _seqs = []
    for seq in seqs:
        _seq = []
        for iden in seq:
            _seq.extend(iden2chunks[iden])
        _seqs.append(_seq)
    f.write("\n".join([" ".join(seq) for seq in _seqs]))
    f.flush()
    f.close()

def convert_ast_to_graph(ast, identifiers):
    ## solve member reference and method invocation
    # graph = nx.DiGraph()
    # node_id = 0
    distance_table = dict()
    paths = list()
    for path, ast_node in ast:
        for child in ast_node.children:
            if not isinstance(child, str) or child not in identifiers:
                continue
            path += (child, )
            paths.append(path)
    for path1, path2 in itertools.combinations(paths, 2):
        offset = max(max(len(path1), len(path2)) - MAX_DIS, 0)
        index = 0
        for i, (ele1, ele2) in enumerate(zip(path1[offset:], path2[offset:])):
            if ele1 is not ele2:
                index = i
                break
        dis = len(path1[index:]) + len(path2[index:])
        if dis > MAX_DIS:
            continue
        if (path1[-1], path2[-1]) in distance_table and dis >= distance_table[path1[-1], path2[-1]]:
            continue
        distance_table[path1[-1], path2[-1]] = dis
        distance_table[path2[-1], path1[-1]] = dis
    return distance_table

def random_walk(distance_table):
    seqs = list()
    neighbour_table = defaultdict(list)
    for (u, v), dis in distance_table.items():
        neighbour_table[u].append((v, dis))
    # print(neighbour_table)
    for u, out_edges in list(neighbour_table.items()):
        neighbours, distances = zip(*out_edges)
        total_dis = sum(distances)
        weights = [math.log2(total_dis / dis) for dis in distances]
        total_weight = sum(weights)
        normal_weights = [w / total_weight if total_weight > 0 else 1. for w in weights]
        neighbour_table[u] = neighbours, normal_weights
    # print(neighbour_table)
    
    for identifier in neighbour_table:
        for _ in range(NUM_SEQ):
            seq = list()
            hop = 0
            cur_identifier = identifier
            while hop < MAX_SEQ_LEN:
                # seq.extend(slicer.slice(cur_identifier))
                seq.append(cur_identifier)
                neighbours, probs = neighbour_table[identifier]
                cur_identifier = np.random.choice(neighbours, 1, probs)[0]
                hop += 1
            seqs.append(seq)
    return seqs

def train(corpus_files, wv_path):
    class Corpus:
        def __init__(self, fnames):
            self.fnames = fnames
    
        def __iter__(self):
            for fname in self.fnames:
                with Path(fname).open("r", encoding="utf-8") as f:
                    sentences = f.readlines()
                    for sent in sentences:
                        yield sent.split()

    # sentences = iter(line.strip().split() for filename in corpus_files for line in Path(filename).open("r", encoding="utf-8"))
    sentences = Corpus(corpus_files)
    model = Word2Vec(sentences, size=100, window=10, iter=3, min_count=MIN_WORD_COUNT, workers=PROCESSOR_NUM)
    model.wv.save(wv_path)
    # model.wv.save_word2vec_format("codebase/code2vec.txt")

def merge(*seqs_list):
    seqs = list()
    for _seqs in seqs_list:
        seqs.extend(_seqs)
    return seqs
    
if __name__ == "__main__":
    # with Path("samples/Foo.java").open("r", encoding="utf-8") as f:
    #     code = f.read()
    #     ast = parse(code)
    #     graph = convert_ast_to_graph(ast)
    #     for seq in random_walk(graph):
    #         print(seq)

    # filenames = list()
    # output_files = list()
    # for file in Path("codebase").glob("classes-batch*"): 
    #     filenames.append(str(file))
    #     output_files.append(str(file).replace("classes", "code2vec_corpora/corpus").replace(".pkl", ".txt"))
    # print(filenames)
    # print(output_files)
    # start_time = time.time()
    # pool = multiprocessing.Pool(PROCESSOR_NUM)
    # results = []
    # for input_file, output_file in zip(filenames, output_files):
    #     rs = pool.apply_async(generate_corpus, args=(input_file, output_file))
    #     results.append(rs)
    # pool.close()
    # pool.join()
    # [rs.get() for rs in results]
    # print(f"time: {time.time() - start_time}s")
    
    start_time = time.time()
    corpus_filenames = list(str(filename) for filename in Path("codebase/code2vec_corpora").glob("corpus-batch*"))
    print("train wv...")
    train(corpus_filenames, "codebase/code2vec_corpora/code2vec.bin")
    # # corpus = merge(*[rs.get() for rs in results])
    end_time = time.time()
    print(f"time: {end_time - start_time}s")

    # with Path(f"codebase/corpus.pkl").open("wb") as f:
    #     pickle.dump(corpus, f)
