#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from nltk.corpus import wordnet as wn
import re

from .resource import DEFAULT_DICT

class POSCandidateProvider:
    def __init__(self, dictionary=DEFAULT_DICT):
        self.dictionary = dictionary
        self.pos_cache = {}

    def provide(self, phrase):
        words = phrase.split()
        tags = []
        for word in words:
            candidates = []
            if self.isArtical(word):
                tags.append((word, ["art"]))
                continue
            if self.isPreposition(word):
                tags.append((word, ["prep"]))
                continue
            if self.isQuantifier(word):
                tags.append((word, ["quant"]))
                continue
            if self.isIrregularV(word):
                candidates.append("irV")
            if self.isAdverb(word):
                candidates.append("adv")
            if self.isPronoun(word):
                candidates.append("pron")
            if self.isAdjective(word):
                candidates.append("adj")
            if self.isNoun(word):
                candidates.append("noun")
            if self.isPlNoun(word):
                # if len(candidates) > 0 and candidates[-1] == "noun":
                #     candidates.pop()
                candidates.append("plN")
            if self.is3PS(word):
                candidates.append("3PS")
            if self.isBaseVerb(word):
                # if not (len(candidates) > 0 and candidates[-1] == "3PS"):    
                candidates.append("baseV")
            if self.isIngVerb(word):
                # if len(candidates) > 0 and candidates[-1] == "baseV":
                #     candidates.pop()
                candidates.append("ingV")
            if self.isPastVerb(word):
                # if len(candidates) > 0 and candidates[-1] == "baseV":
                #     candidates.pop()
                candidates.append("pastV")
            if self.isPP(word):
                candidates.append("pp")
            if len(candidates) == 0:
                candidates.append("noun")

            tags.append((word, candidates))
        return tags

    def pos_in_wn(self, word):
        lemma = word.lower()
        if lemma in self.pos_cache:
            return self.pos_cache[lemma]

        get_synset = wn.synset_from_pos_and_offset
        index = wn._lemma_pos_offset_map
        synsets = [
            get_synset(p, offset)
            for p in [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]
            for offset in index[lemma].get(p, [])
        ]
        self.pos_cache[lemma] = {s.pos() for s in synsets}
        return self.pos_cache[lemma]
            

    def isArtical(self, word):
        if word in {"a", "an", "the"}:
            return True
        return  False

    def isPreposition(self, word):
        if word in self.dictionary["PREP"]:
            return True
        return False

    def isQuantifier(self, word):
        if word in self.dictionary["QUAN"]:
            return True
        return False

    def isIrregularV(self, word):
        if word in self.dictionary["IRRV"]:
            return True
        return False

    def isAdverb(self, word:str):
        if word in self.dictionary["ADV"]:
            return True
        wn_pos = self.pos_in_wn(word)
        if wn.ADV in wn_pos:
            self.dictionary["ADV"].add(word)
            
            return True
        if len(wn_pos) > 0 and len(wn_pos & {wn.VERB, wn.NOUN, wn.ADJ, wn.ADV, wn.ADJ_SAT}) > 0:
            return False
        if word.endswith("ly"):
            base = word[:-2]
            if len(base) > 0 and base[-1] == "i":
                base = base[:-1] + "y"
            if base in self.dictionary["VOCAB"]:
                self.dictionary["ADV"].add(word)
                
                return True
        return False

    def isPronoun(self, word):
        if word in self.dictionary["PRON"]:
            return True
        return False

    def isAdjective(self, word:str):
        if word in self.dictionary["ADJ"]:
            return True
        wn_pos = self.pos_in_wn(word)
        if wn.ADJ in wn_pos or wn.ADJ_SAT in wn_pos:
            self.dictionary["ADJ"].add(word)
            
            return True
        if len(wn_pos) > 0 and len(wn_pos & {wn.VERB, wn.NOUN, wn.ADJ, wn.ADV, wn.ADJ_SAT}) > 0:
            return False
        if word.endswith("able") and len(word) > 6:
            self.dictionary["ADJ"].add(word)
            
            return True
        if word.endswith("er") or word.endswith("est"):
            if word.endswith("er"):
                base = word[:-2]
            else:
                base = word[:-3]
            
            if len(base) > 0 and base[-1] == "i":
                base = base[:-1] + "y"
            if len(base) >= 2 and base[-1] == base[-2]:
                base = base[:-1]
            if self.isAdjective(base):
                self.dictionary["ADJ"].add(word)
                
                return True
        prefix = word
        if len(word) > 1 and word.endswith("y") and word[-2] not in {"a", "e", "i", "o", "u"}:
            prefix = word[:-1] + "i"
        if prefix + "ly" in self.dictionary["VOCAB"] or prefix + "ness" in self.dictionary["VOCAB"]:
            self.dictionary["ADJ"].add(word)
            
            return True

        return False

    def isNoun(self, word:str):
        if word in self.dictionary["NOUN"]:
            return True
        wn_pos = self.pos_in_wn(word)
        if wn.NOUN in wn_pos:
            return True
        if len(wn_pos) > 0 and len(wn_pos & {wn.VERB, wn.NOUN, wn.ADJ, wn.ADV, wn.ADJ_SAT}) > 0:
            return False
        if word + "ence" in self.dictionary["VOCAB"] or  word + "ance" in self.dictionary["VOCAB"]:
            return False
        if word in self.dictionary["NABBR"]:
            return True
        elif self.isIrregularV(word):
            return False
        if re.match(r"^.+(ity|tion|is[tm]|ness|or)$", word):
            self.dictionary["NOUN"].add(word)
            
            return True

        prefix = re.sub(r"([^aeiou])y$", r"\1i", word)
        if re.match(r"^.*(i|s|ch|x|z|sh)$", prefix) and prefix + "es" in self.dictionary["VOCAB"]:
            self.dictionary["NOUN"].add(word)
            return True

        if word + "s" in self.dictionary["VOCAB"]:
            self.dictionary["NOUN"].add(word)
            
            return True

        return False

    def isPlNoun(self, word:str):
        base = word
        if word.endswith("es"):
            base = word[:-2]
            if len(base) > 1 and base.endswith("i") and base[-2] not in {"a", "e", "i", "o", "u"}:
                base = base[:-1] + "y"
            if self.isNoun(base) and re.match(r"^.*(y|s|ch|x|z|sh)$", base):
                return True
        if re.match(r"(.*[^sui])s$", word) and len(word) > 3 and wn.NOUN in self.pos_in_wn(word[:-1]):
            return True
        if re.match(r"(.*[^sui])s$", word) and len(word) > 4 and self.isNoun(word[:-1]):
            return True
        return False

    def is3PS(self, word:str):
        if re.match(r"(.*[^sui])s$", word):
            base = word[:-1]
            base = re.sub(r"ie$", "y", base)
            if self.isBaseVerb(base):
                return True
        return False

    def isBaseVerb(self, word):
        origin = word
        if word in self.dictionary["VERB"]:
            return True
        if self.isIrregularV(word):
            return False
        if wn.VERB in self.pos_in_wn(word):
            return True
        if len(self.pos_in_wn(word)) > 0 and len(self.pos_in_wn(word) & {wn.VERB, wn.NOUN, wn.ADJ, wn.ADV, wn.ADJ_SAT}) > 0:
            return False

        if word not in self.dictionary["VOCAB"] or len(word) < 2:
            return False

        if re.match(r"^(re|en).*", word) and self.isBaseVerb(word[2:]):
            return True
        if re.match(r"(.*)(ize|ify)$", word):
            return True

        double = word
        if re.match(r"[aeiou][ngdtlp]$", word):
            double += double[-1]
        elif re.match(r".*([^ey])e$", word):
            word = word[:-1]
        elif re.match(r"^.*y$", word):
            word = word[:-1] + "i"
        
        if word + "s" in self.dictionary["VOCAB"] or word + "es" in self.dictionary["VOCAB"] or double + "es" in self.dictionary["VOCAB"]:
            if word + "ing" in self.dictionary["VOCAB"] or double + "ing" in self.dictionary["VOCAB"]:
                self.dictionary["VERB"].add(origin)
                self.dictionary["VOCAB"].add(origin)
                return True
            if word + "ed" in self.dictionary["VOCAB"] or double + "ed" in self.dictionary["VOCAB"]:
                self.dictionary["VERB"].add(origin)
                self.dictionary["VOCAB"].add(origin)
                return True
        return False

    def isIngVerb(self, word:str):
        if word.endswith("ing") and self.isBaseVerb(word[:-3]):
            return True
        return False

    def isPastVerb(self, word:str):
        if word.endswith("ed") and self.isBaseVerb(word[:-2]):
            return True
        return False

    def isPP(self, word:str):
        if word in self.dictionary["PP"]:
            return True
        elif re.match(r"(.*)e[nd]$", word):
            base = word[:-2]
            base = re.sub(r"i$", "y", base)
            if self.isBaseVerb(base) or self.isBaseVerb(base + "e") or self.isBaseVerb(base[:-1]):
                return True
        return False

