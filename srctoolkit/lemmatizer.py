#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import functools
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

LEMMATIZER = WordNetLemmatizer()

class Lemmatizer:
    @functools.lru_cache(maxsize=10000)
    def lemmatize_noun(noun):
        lower = noun.lower()
        return LEMMATIZER.lemmatize(lower, "n")

    @functools.lru_cache(maxsize=10000)
    def lemmatize_np(np):
        return " ".join([Lemmatizer.lemmatize_noun(word) for word in np.split()])

    @functools.lru_cache(maxsize=10000)
    def lemmatize_verb(verb):
        lower = verb.lower()
        words = lower.split()
        lemma = " ".join([LEMMATIZER.lemmatize(words[0], "v")] + words[1:])
        return lemma

    @functools.lru_cache(maxsize=10000)
    def check_verb(word, rate_thres=0.6, count_thres=10):
        pos2count = dict()
        for synset in wordnet.synsets(word):
            lemma, pos, _ = synset.name().split(".")
            pos2count[pos] = pos2count.get(pos, 0) + 1
        # logging.info(pos2count)
        if len(pos2count) > 0 and (pos2count.get("v", 0) >= count_thres or pos2count.get("v", 0) / sum(pos2count.values()) >= rate_thres):
            return True
        return False

    # @functools.lru_cache(maxsize=10000)
    # def check_noun(word, rate_thres=0.5):
    #     pos2count = dict()
    #     for synset in wordnet.synsets(word):
    #         parts = synset.name().split(".")
    #         if len(parts) != 3:
    #             continue
    #         lemma, pos, _ = parts
    #         pos2count[pos] = pos2count.get(pos, 0) + 1
    #     # logging.info(pos2count)
    #     if len(pos2count) == 0:
    #         return True
    #     if pos2count.get("n", 0) / sum(pos2count.values()) >= rate_thres:
    #         return True
    #     return False

    @functools.lru_cache(maxsize=10000)
    def check_noun(word):
        # logging.info(nltk.pos_tag([word]))
        return nltk.pos_tag([word])[0][1] in {"NN", "NNS"}

    # @functools.lru_cache(maxsize=10000)
    # def check_noun(word, rate_thres=0.5):
    #     pos2count = dict()
    #     for synset in wordnet.synsets(word):
    #         parts = synset.name().split(".")
    #         if len(parts) != 3:
    #             continue
    #         lemma, pos, _ = parts
    #         pos2count[pos] = pos2count.get(pos, 0) + 1
    #     # logging.info(pos2count)
    #     if len(pos2count) == 0:
    #         return True
    #     if pos2count.get("n", 0) / sum(pos2count.values()) >= rate_thres:
    #         return True
    #     return False