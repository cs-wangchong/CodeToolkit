#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path
import pickle
import math
import time
import multiprocessing
import logging

from codetoolkit.code2vec import  _extract_for_code, generate_corpus, train


if __name__ == "__main__":
    # with Path("test/Sample1.java").open("r", encoding="utf-8") as f:
    #     code = f.read()
    #     seqs, vocab = _extract_for_code(code)
    #     print(vocab)
    #     for seq in seqs:
    #         print(seq)

    format = '[%(levelname)s] %(asctime)s - %(pathname)s[line:%(lineno)d] - %(message)s'
    logging.basicConfig(level=logging.INFO, format=format)
    formatter = logging.Formatter(format)
    file_handler = logging.FileHandler(filename="test/code2vec.log", mode="w", encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(file_handler)
            

    inp_files = list()
    seq_files = list()
    meta_files = list()
    for file in Path("/home/Data/SemanticTagging/codebase").glob("classes-batch*"):
        batch_id = file.parts[-1].split(".")[-2][len("classes-batch"):]
        inp_files.append(str(file))
        seq_files.append(f"/home/Data/CodeToolkit/code2vec/sequence_corpus-batch{batch_id}.txt")
        meta_files.append(f"/home/Data/CodeToolkit/code2vec/sequence_corpus_meta-batch{batch_id}.pkl")
    print(inp_files)
    start_time = time.time()
    pool = multiprocessing.Pool(len(inp_files))
    results = []
    for input_file, output_file, vocab_file in zip(inp_files, seq_files, meta_files):
        rs = pool.apply_async(generate_corpus, args=(input_file, output_file, vocab_file))
        results.append(rs)
    pool.close()
    pool.join()
    # [rs.get() for rs in results]
    print(f"generate corpus time: {time.time() - start_time}s")

    start_time = time.time()
    train(seq_files, meta_files, "/home/Data/CodeToolkit/code2vec/emb.bin")
    
# #     start_time = time.time()
# #     corpus_filenames = list(str(filename) for filename in Path("codebase/code2vec_corpora").glob("corpus-batch*"))
# #     print("train wv...")
# #     train(corpus_filenames, "codebase/code2vec_corpora/code2vec.bin")
# #     # # corpus = merge(*[rs.get() for rs in results])
# #     end_time = time.time()
# #     print(f"time: {end_time - start_time}s")

# #     # with Path(f"codebase/corpus.pkl").open("wb") as f:
# #     #     pickle.dump(corpus, f)
