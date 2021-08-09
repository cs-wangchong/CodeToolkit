#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import spacy
import re
import functools

from .posse.tagger import Tagger
# from .nlp import NLP

class CodePOS:
    __INSTANCE = None

    def __init__(self):
        self.tagger = Tagger()
        self.secondary_tagger = NLP.get_inst()

    def __call__(self, method_name):
        return self.tag(method_name)

    @functools.lru_cache(maxsize=10000)
    def tag(self, method_name):
        name_pos = None
        name_words = method_name.lower().split()

        if len(name_words) == 0:
            return []

        if name_words[0] == "to" and len(name_words) > 1:
            return [("to", "closedlist")] + [(word, "noun") for word in name_words[1:]]

        if name_words[0] == "new" and len(name_words) > 1:
            return [("new", "verb")] + [(word, "noun") for word in name_words[1:]]

        indices = []
        for index, word in enumerate(name_words):
            if word in {"and", "or"}:
                indices.append(index)
        starts = [0] + [idx + 1 for idx in indices]
        ends = indices + [len(name_words)]
        segments = [" ".join(name_words[start:end]).strip() for start, end in list(zip(starts, ends))]
        pos = []
        queue = []
        while len(segments) > 0:
            segment = segments.pop(0)
            if len(segment) == 0:
                continue
            queue.append(segment)
            segment_pos = self.tagger.tag(" ".join(queue), False)
            # logging.info(segment_pos)
            if segment_pos is None:
                break
            word, tag = segment_pos.eles[0]
            if tag == "verb":
                if len(indices) > 0 and len(pos) == indices[0]:
                    pos.append((name_words[indices[0]], "conj"))
            pos.extend(segment_pos.eles)
            queue = []
        if len(indices) > 0 and len(pos) == indices[0]:
            pos.append((name_words[indices[0]], "conj"))
        if len(pos) == len(name_words):
            name_pos = pos

        # tagging_result = self.tagger.tag(method_name, False)
        # if tagging_result is None:
        #     name_words = method_name.split()
        #     indices = []
        #     for index, word in enumerate(name_words):
        #         if word.lower() in {"and", "or"}:
        #             indices.append(index)
        #     starts = [0] + [idx + 1 for idx in indices]
        #     ends = indices + [len(name_words)]
        #     segments = [" ".join(name_words[start:end]).strip() for start, end in list(zip(starts, ends))]
        #     pos = []
        #     queue = []
        #     while len(segments) > 0:
        #         segment = segments.pop(0)
        #         if len(segment) == 0:
        #             continue
        #         queue.append(segment)
        #         segment_pos = self.tagger.tag(" ".join(queue), False)
        #         if segment_pos is None:
        #             break
        #         word, tag = segment_pos.eles[0]
        #         if tag == "verb":
        #             if len(indices) > 0 and len(pos) == indices[0]:
        #                 pos.append((name_words[indices[0]], "conj"))
        #             pos.extend(segment_pos.eles)
        #             queue = []
        #     if len(indices) > 0 and len(pos) == indices[0]:
        #         pos.append((name_words[indices[0]], "conj"))
        #     if len(pos) == len(name_words):
        #         name_pos = pos
        # else:
        #     name_pos = tagging_result.eles
        # print(name_pos)
        if name_pos is None:
            name_pos = []
            for token in self.secondary_tagger.parse(method_name):
                word = token.text
                tag = token.pos_.lower()
                if tag == "adp":
                    tag = "closedlist"
                if tag == "aux":
                    tag = "verb"
                name_pos.append((word, tag))
        return name_pos

    @classmethod
    def get_inst(cls, *args):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls()
        return cls.__INSTANCE

def pos(method_name):
    return CodePOS.get_inst().tag(method_name)
