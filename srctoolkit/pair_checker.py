#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import textdistance
import itertools
import functools
import numpy as np

from .lemmatizer import Lemmatizer

DLDis = textdistance.DamerauLevenshtein()
LCSSeq = textdistance.LCSSeq()

class PairChecker:
    
    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def normalize(term):
        lemma = Lemmatizer.lemmatize_noun(term)
        name = lemma.replace("-", " ")
        name = re.sub(r"\s+", " ", name)
        return name

    @staticmethod
    def check_synonym(long_term, short_term, lemma=True, max_dis=2, threshold=0.25):
        if long_term.isupper() and short_term.isupper():
            return False
        # if long_term.lower().rstrip("s") == short_term.lower().rstrip("s"):
        #     return True
        if lemma:
            long_term = PairChecker.normalize(long_term)
            short_term = PairChecker.normalize(short_term)

        if long_term == short_term:
            return True
        if long_term.replace(" ", "") == short_term.replace(" ", ""):
            return True

        long_words = long_term.split()
        short_words = short_term.split()

        if len(long_words) != len(short_words):
            return False
        for word1, word2 in zip(long_words, short_words):
            if word1[0] != word2[0]:
                return False
            if re.findall(r'[0-9]+', word1) != re.findall(r'[0-9]+', word2):
                return False
            if DLDis.distance(word1, word2) > max_dis or DLDis.normalized_distance(word1, word2) >= threshold:
                return False
        return True

    @staticmethod
    def __check_word_word(long_word, short_word, thres=2/3):
        if re.match(r'^[0-9]+$', long_word) or re.match(r'^[0-9]+$', long_word):
            return False
        if long_word[0] != short_word[0]:
            return False
        if len(short_word) / len(long_word) >= thres:
            return False
        # logging.info(long_word, short_word, LCSSeq.similarity(long_word, short_word))
        if LCSSeq.similarity(long_word, short_word) != len(short_word):
            return False
        
        # check prefix
        if long_word.startswith(short_word):
            return True
        # check acronym
        if len(set(short_word) & {"a", "e", "i", "o", "u"}) == 0:
            return True
        return False

    @staticmethod
    def __check_phrase_word(phrase, word):
        if phrase[0] != word[0]:
            return False
        words = phrase.split()
        if len(word) < len(words):
            return False
        if len(words) == 1:
            return PairChecker.__check_word_word(phrase, word)
        else:
            if words[0] == word or len(words) != len(word):
                return False
            for indices in itertools.combinations([i for i in range(1, len(word), 1)], len(words) - 1):
                # logging.info(indices)
                copied_words = words.copy()
                indices = (0, ) + indices + (len(word), )
                # logging.info(indices)
                pairs = [(beg, end) for (beg, end) in zip(indices[:-1], indices[1:])]
                beg, end = pairs.pop(0)
                cur_chars = word[beg:end]
                
                cur_word = copied_words.pop(0)
                # logging.info(cur_chars, cur_word)
                if cur_chars[0] == cur_word[0]:
                    if not PairChecker.__check_word_word(cur_word, cur_chars):
                        continue
                elif cur_word[0] in set("aeiou") and len(cur_word) > 1 and cur_chars[0] == cur_word[1]:
                    if end != 1:
                        continue
                else:
                    continue

                for (beg, end), cur_word in zip(pairs, copied_words):
                    cur_chars = word[beg:end]
                    # logging.info(cur_chars, cur_word)
                    if not PairChecker.__check_word_word(cur_word, cur_chars):
                        break
                else:
                    return True

            return False

    @staticmethod
    def check_abbr(long_term, short_term, lemma=True):
        if lemma:
            long_term = PairChecker.normalize(long_term)
            short_term = PairChecker.normalize(short_term)

        # logging.info(long_term, short_term)

        if len(short_term.split()) == 1:
            return PairChecker.__check_phrase_word(long_term, short_term)
        else:
            short_words = short_term.split()
            long_words = long_term.split()
            if len(long_words) < len(short_words):
                return False
            while len(short_words) > 0 and short_words[0] == long_words[0]:
                short_words.pop(0)
                long_words.pop(0)
            while len(short_words) > 0 and short_words[-1] == long_words[-1]:
                short_words.pop(-1)
                long_words.pop(-1)
            if len(short_words) == 1:
                return PairChecker.__check_phrase_word(" ".join(long_words), short_words[0])
            elif len(short_words) == len(long_words):
                for word1, word2 in zip(long_words, short_words):
                    if not PairChecker.__check_word_word(word1, word2):
                        return False
                return True
            return False