#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   Chong Wang 
@Contact :   chongwang18@fudan.edu.cn
@Time    :   2019/12/17
'''

from pathlib import Path
import functools

from .lemmatizer import Lemmatizer
from .dictionary import PREPOSITIONS, PHRASAL_VERBS


class CodeChunker:
    __INSTANCE = None

    def __init__(self):
        pass

    def __call__(self, name, *verbs):
        return self.chunk(name, *verbs)
    
    def complete_verb(self, lemma, words, verb):
        verb_eles = [verb]
        word_num = len(words)
        if lemma in PHRASAL_VERBS and word_num > 0:
            len2verb = {}
            for pred in PHRASAL_VERBS[lemma]:
                length = len(pred.split())
                if length > word_num:
                    continue
                if length not in len2verb:
                    len2verb[length] = set()
                len2verb[length].add(pred)
            for length, preds in len2verb.items():
                candidate = " ".join([lemma] + words[:length - 1])
                if candidate in preds:
                    verb_eles.extend(words[:length - 1])
                    break
        return " ".join(verb_eles)
        
    
    @functools.lru_cache(maxsize=10000)
    def chunk(self, name, *verbs):
        verbs = {Lemmatizer.lemmatize_verb(verb) for verb in verbs}
        words = name.lower().split()
        size = len(words)
        if size == 0:
            return None
        lemmas = [Lemmatizer.lemmatize_verb(word) for word in words]
        
        segments = [[]]
        idx = 0
        while idx < size:
            word = words[idx]
            lemma = lemmas[idx]
            if word in {"and", "or"} and 0 < idx < size - 1 and (lemmas[idx - 1] in verbs or lemmas[idx + 1] in verbs):
                segments.append([(words[idx + 1], lemmas[idx + 1])])
                idx += 2
            else:
                segments[0].append((word, lemma))
                idx += 1
        # logging.info(segments)
        verb2chunks = {}
        for segment in segments:
            verb = None
            chunks = []
            chunk = []

            while len(segment) > 0:
                word, lemma = segment.pop(0)
                if lemma in verbs:
                    verb = self.complete_verb(lemma, [w for w, _ in segment], word)

                    for _ in range(len(verb.split()) - 1):
                        segment.pop(0)
                    if len(chunk) > 0:
                        chunks.append(" ".join(chunk))
                        chunk = []
                    chunks.append(verb)
                elif word in PREPOSITIONS:
                    if len(chunk) > 0:
                        chunks.append(" ".join(chunk))
                        chunk = []
                    chunks.append(word)
                else:
                    chunk.append(word)
            if len(chunk) > 0:
                chunks.append(" ".join(chunk))
            verb2chunks[verb] = chunks

        rests = []
        for verb, chunks in verb2chunks.items():
            for idx, chunk in enumerate(chunks):
                if chunk == verb:
                    rests.append(chunks[idx + 1:])
                    break
            else:
                rests.append([])
        for idx, (verb, chunks) in enumerate(verb2chunks.items()):
            if len(rests[idx]) == 0:
                if idx > 0 and len(rests[idx - 1]) > 0:
                    verb2chunks[verb] += rests[idx - 1]
                elif idx < len(rests) - 1 and len(rests[idx + 1]) > 0:
                    verb2chunks[verb] += rests[idx + 1]

        return verb2chunks

    @classmethod
    def get_inst(cls, *args):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls()
        return cls.__INSTANCE

def chunk(name, *verbs):
    return CodeChunker.get_inst().chunk(name, *verbs)



                    
