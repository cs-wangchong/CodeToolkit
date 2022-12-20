#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path
import pickle
import math
import time
import multiprocessing
import logging
import itertools

import numpy as np
from gensim.models.fasttext import FastTextKeyedVectors

from codetoolkit.code2vec import  _extract_for_code, generate_corpus, train


if __name__ == "__main__":

    # with Path("test/Sample1.java").open("r") as f:
    #     code  = f.read()
    # seqs, vocab = _extract_for_code(code, level="class")
    # print(vocab)
    # for seq in seqs:
    #     print(seq)

    # format = '[%(levelname)s] %(asctime)s - %(pathname)s[line:%(lineno)d] - %(message)s'
    # logging.basicConfig(level=logging.INFO, format=format)
    # formatter = logging.Formatter(format)
    # file_handler = logging.FileHandler(filename="test/code2vec-classlevel.log", mode="w", encoding='utf-8')
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.INFO)
    # logging.getLogger().addHandler(file_handler)
            

    # inp_files = list()
    # seq_files = list()
    # meta_files = list()
    # for file in Path("/home/Data/SemanticTagging/codebase").glob("classes-batch*"):
    #     batch_id = file.parts[-1].split(".")[-2][len("classes-batch"):]
    #     inp_files.append(str(file))
    #     seq_files.append(f"/home/Data/CodeToolkit/code2vec/sequence_corpus-classlevel-batch{batch_id}.txt")
    #     meta_files.append(f"/home/Data/CodeToolkit/code2vec/sequence_corpus_meta-classlevel-batch{batch_id}.pkl")
    # print(inp_files)

    # start_time = time.time()
    # pool = multiprocessing.Pool(len(inp_files))
    # results = []
    # for input_file, output_file, vocab_file in zip(inp_files, seq_files, meta_files):
    #     rs = pool.apply_async(generate_corpus, args=(input_file, output_file, vocab_file, "class"))
    #     results.append(rs)
    # pool.close()
    # pool.join()
    # print(f"generate corpus time: {time.time() - start_time}s")

    # start_time = time.time()
    # train(seq_files, meta_files, model_path="/home/Data/CodeToolkit/code2vec/fasttext-classlevel.bin", emb_path="/home/Data/CodeToolkit/code2vec/emb-classlevel.bin", fine_tuning=True, epochs=2)
    # print(f"train token vectors: {time.time() - start_time}s")




    # with Path(f"/home/Data/CodeToolkit/code2vec/sequence_corpus-batch1.txt").open("r", encoding="utf-8") as f:
    #     for i, line in enumerate(f):
    #         print(line.strip())
    #         if i >= 10000:
    #             break
        

    def cos(code2vec, word1, word2):
        words1 = word1.split()
        words2 = word2.split()
        vecs1 = [code2vec.get_vector(w) for w in words1]
        vecs2 = [code2vec.get_vector(w) for w in words2]
        vec1 = sum(vecs1) / len(vecs1)
        vec2 = sum(vecs2) / len(vecs2)
        # print(sum(vec1), sum(vec2))
        cos = np.dot(vec1, vec2) / np.linalg.norm(vec1) / np.linalg.norm(vec2)
        return cos / 2 + 0.5

    def pair_cos(code2vec, pair1, pair2):
        vec1 = code2vec.get_vector(pair1[0]) - code2vec.get_vector(pair1[1])
        vec2 = code2vec.get_vector(pair2[0]) - code2vec.get_vector(pair2[1])
        # print(sum(vec1), sum(vec2))
        cos = np.dot(vec1, vec2) / np.linalg.norm(vec1) / np.linalg.norm(vec2)
        return cos / 2 + 0.5

    code2vec: FastTextKeyedVectors = FastTextKeyedVectors.load("/home/Data/ResOpMining/CodeSearchData/code_search_emb-methodlevel.bin")

    # print(code2vec.most_similar("md5sum", topn=100))
    # print(code2vec.most_similar("md5", topn=100))
    # print(code2vec.most_similar("db", topn=100))

    # print(code2vec.most_similar("row", topn=100))
    # print(code2vec.most_similar("col", topn=100))

    # print(code2vec.most_similar("statement", topn=100))
    # print(code2vec.most_similar("stmt", topn=100))

    # keywords = {('input', 'input'), ('file', 'files'), ('message', 'message'), ('digest', 'digest'), ('input stream', 'input stream'), ('message digest', 'message digest'), ('md5', 'md5'), ('path', 'paths')}
    # for (w1, _), (w2, _) in itertools.combinations(keywords, 2):
    #     print(w1, w2, cos(code2vec, w1, w2))
    
    # print("database" in code2vec)
    # print("luminance" in code2vec)
    # print("lum" in code2vec)
    # print("md5" in code2vec)
    # for word, sim in code2vec.most_similar("md5sum", topn=100000):
    #     print(word, sim)
    # print(cos(code2vec, "clear", "reset"))
    # print(cos(code2vec, "substr", "substring"))
    # print(cos(code2vec, "rows", "columns"))
    # print(cos(code2vec, "db", "database"))
    # print(cos(code2vec, "md5", "file"))
    
    # print(cos(code2vec, "rr", "repfdsafsda"))
    # print(cos(code2vec, "x", "y"))

    print(pair_cos(code2vec, ['lock', 'acquire'], ['unlock', 'release']))