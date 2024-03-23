#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from pathlib import Path
import os
from typing import List

from .candidate_provider import POSCandidateProvider
from .resource import DEFAULT_METHOD_CORPUS, DEFAULT_FIELD_CORPUS

class Node:
    def __init__(self, eles:List, tag:str):
        self.eles = eles
        self.tag = tag

    def __str__(self):
        return f"[{' '.join(str(ele) for ele in self.eles)}]:{self.tag}"

class Chunker:
    def __init__(self, provider=POSCandidateProvider(), word_freq:dict=None):
        self.provider = provider
        self.word_freq = word_freq
        if word_freq is None:
            self.__init_ferq_from_files(DEFAULT_METHOD_CORPUS, DEFAULT_FIELD_CORPUS)


    @classmethod
    def from_path(cls, method_path, field_path):
        instance = cls(POSCandidateProvider(), {})
        instance.__init_ferq_from_files(method_path, field_path)
        return instance

    
    def __init_ferq_from_files(self, method_path, field_path):
        word_freq = {}
        with Path(method_path).open("r", encoding="utf-8") as f:
            for line in f:
                words = line.strip().split()
                if words[0] not in word_freq:
                    word_freq[words[0]] = {}
                if words[-1] not in word_freq:
                    word_freq[words[-1]] = {}

                if len(words) == 1:
                    word_freq[words[0]]["method-single"] = word_freq[words[0]].get("method-single", 0) + 1
                else:
                    word_freq[words[0]]["method-begin"] = word_freq[words[0]].get("method-begin", 0) + 1
                    word_freq[words[-1]]["method-end"] = word_freq[words[-1]].get("method-end", 0) + 1
        with Path(field_path).open("r", encoding="utf-8") as f:
            for line in f:
                words = line.strip().split()
                if words[0] not in word_freq:
                    word_freq[words[0]] = {}
                if words[-1] not in word_freq:
                    word_freq[words[-1]] = {}

                if len(words) == 1:
                    word_freq[words[0]]["field-single"] = word_freq[words[0]].get("field-single", 0) + 1
                else:
                    word_freq[words[0]]["field-begin"] = word_freq[words[0]].get("field-begin", 0) + 1
                    word_freq[words[-1]]["field-end"] = word_freq[words[-1]].get("field-end", 0) + 1
        self.word_freq = word_freq

    def get_score(self, word):
        if word not in self.word_freq:
            return 0
        # print(self.word_freq[word])
        nverb = self.word_freq[word].get("method-begin", 0) + self.word_freq[word].get("field-single", 0)
        nnoun = self.word_freq[word].get("method-end", 0) + self.word_freq[word].get("field-single", 0) + self.word_freq[word].get("field-end", 0)
        if (nverb + nnoun) == 0:
            return 0
        return nverb / (nverb + nnoun)

    def chunk(self, phrase, is_construction):
        
        phrase = self.provider.provide(phrase)
        if is_construction:
            node = Node([" ".join(word for word, _ in phrase)], "NP")
            return Node([node], "ROOT")
        head, head_tags = phrase[0]
        if self.isSomeVerb(head_tags) and self.isSomeNoun(head_tags):
            score = self.get_score(head)
            # print(score)
            if score >= 0.8:
                phrase[0] = (head, ["baseV"])
            elif 0 < score <= 0.1:
                phrase[0] = (head, ["noun"])
        tail, tail_tags = phrase[-1]
        if self.isSomeVerb(tail_tags) and self.isSomeNoun(tail_tags):
            score = self.get_score(tail)
            if score >= 0.8:
                phrase[-1] = (tail, ["baseV"])
            elif 0 < score <= 0.2:
                phrase[-1] = (tail, ["noun"])

        rule_flag = False
        if not self.isSomeVerb(phrase[0][1]) and self.isSomeVerb(phrase[-1][1]):
            rule_flag = True

        if len(phrase) > 1 and "pp" in phrase[-1][1]:
            phrase[-2] = (phrase[-2][0], ["noun"])
        
        if len(phrase) > 1:
            first, first_tags = phrase[0]
            second, second_tags = phrase[1]
            first_score = self.get_score(first)
            second_score = self.get_score(second)
            if len(first_tags) == 1 and self.isSomeNoun(first_tags) and self.isSomeVerb(second_tags):
                if second_score > 0.3:
                    phrase[0] = (phrase[0][0], ["adv"])
            if len(second_tags) == 1 and (not self.isSomeVerb(first_tags)) and self.isSomeVerb(second_tags):
                if second_score > 0.3:
                    phrase[0] = (phrase[0][0], ["adv"])
            if self.isSomeVerb(first) and self.isSomeVerb(second):
                if second_score >= 0.8 and first_score <= 0.2:
                    phrase[0] = (phrase[0][0], ["adv"])
                elif second_score >= 0.99 and first_score <= 0.4:
                    phrase[0] = (phrase[0][0], ["adv"])

        output = self.NPVP(phrase[:])
        if rule_flag and output is not None:
            return output
        output = self.startsWithIsOrCan(phrase[:])
        if output is not None:
            return output
        output = self.VPPP(phrase[:])
        if output is not None:
            return output
        output = self.PP(phrase[:])
        if output is not None:
            return Node([output], "ROOT")
        output = self.VPNP(phrase[:])
        if output is not None:
            return output
        output = self.VPp(phrase[:])
        if output is not None:
            return output
        output = self.VPNM(phrase[:])
        if output is not None:
            return output
        output = self.VP(phrase[:])
        if output is not None:
            return Node([output], "ROOT")
        output = self.VPNPprepP(phrase[:])
        if output is not None:
            return output
        output = self.VPprepP(phrase[:])
        if output is not None:
            return output
        output = self.adjP(phrase[:])
        if output is not None:
            return Node([output], "ROOT")
        output = self.NP(phrase[:])
        if output is not None:
            return Node([output], "ROOT")
        output = self.NPVP(phrase[:])
        if output is not None:
            return output
        output = self.VPadjP(phrase[:])
        if output is not None:
            return output
        output = self.prepP(phrase[:])
        if output is not None:
            return Node([output], "ROOT")
        output = self.VPNPp(phrase[:])
        if output is not None:
            return output
        return None
        

    def VP(self, phrase):
        size = len(phrase)
        if size == 0:
            return None
        if size == 1 and self.isSomeVerb(phrase[0][1]):
            return Node([phrase[0][0]], "VP")
        last = phrase.pop()
        vm = self.VM(phrase[:])
        if size > 1 and vm is not None:
            return Node([vm, last[0]], "VP")
        return None

    def NP(self, phrase):
        if len(phrase) == 0:
            return None
        np_eles = []
        while len(phrase) > 0:
            if "prep" in phrase[0][1]:
                break
            np_eles.append(phrase.pop(0))
        if len(np_eles) == 0:
            return None
        np = None
        if self.isSomeNoun(np_eles[-1][1]) or "ingV" in np_eles[-1][1]:
            word, _ = np_eles.pop()
            if len(np_eles) == 0:
                np = Node([word], "NP")
            else:
                nm = self.NM(np_eles)
                if nm is not None:
                    np = Node([nm, word], "NP")
        if len(phrase) > 0 and np is not None:
            pP = self.prepP(phrase[:])
            if pP is not None and phrase[0][0] == "of":
                np.eles.append(pP)
            else:
                return None
        return np

    def PP(self, phrase):
        if len(phrase) == 0:
            return None
        if "pp" in phrase[-1][1]:
            _is = False
            if len(phrase) == 1:
                return Node([phrase[0][0]], "VP-PP")
            else:
                last = phrase.pop()
                if phrase[-1][0] == "is":
                    _is = True
                    phrase.pop()
                np = self.NP(phrase[:])
                if np is not None:
                    if _is:
                        return Node([np, "is", last[0]], "VP-PP")
                    else:
                        return Node([np, last[0]], "VP-PP")
                else:
                    return None
        return None

    def adjP(self, phrase):
        if len(phrase) == 0:
            return None
        if "adj" in phrase[-1][1]:
            if len(phrase) == 1:
                return Node([phrase[0][0]], "adjP")
            else:
                last = phrase.pop()
                np = self.NP(phrase[:])
                if np is not None:
                    return Node([np, last[0]], "adjP")
        return None

    def prepP(self, phrase):
        if len(phrase) <= 1:
            return None
        first = phrase.pop(0)
        out = self.NP(phrase[:]) 
        out = out if out is not None else self.PP(phrase[:])
        if "prep" in first[1] and out is not None:
            return Node([first[0], out], "prepP")
        return None

    def NM(self, phrase):
        if len(phrase) == 0:
            return None
        nm = []
        for word, tags in phrase:
            if self.isSomeNoun(tags) or self.isSomeVerb(tags) or "adj" in tags or "pp" in tags or "ingV" in tags or "quant" in tags or "pron" in tags or "prep" in tags:
                nm.append(word)
            else:
                return None
        return Node([" ".join(nm)], "NM")

    def VM(self, phrase):
        if len(phrase) == 0:
            return None
        vm = []
        for word, tags in phrase:
            if "adv" in tags:
               vm.append(word)
            else:
                return None
        return Node([" ".join(vm)], "VM")

    def VPNP(self, phrase):
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        np = self.NP(phrase[:])
        if vp is not None and np is not None:
            return Node([vp, np], "ROOT")
        return None

    def NPVP(self, phrase):
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.insert(0, phrase.pop())
            if len(phrase) == 0 or self.isSomeNoun(phrase[-1][1]):
                break
        vp = self.VP(vp_eles)
        np = self.NP(phrase[:])
        if vp is not None and np is not None:
            return Node([np, vp], "ROOT")
        return None

    def VPadjP(self, phrase):
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        ap = self.adjP(phrase[:])
        if vp is not None and ap is not None:
            return Node([vp, ap], "ROOT")
        return None

    def VPNM(self, phrase):
        if len(phrase) == 0:
            return None
        if self.isSomeNoun(phrase[-1][1]):
            return None
        vp_eles = []

        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        nm = self.NM(phrase[:])
        if vp is not None and nm is not None:
            return Node([vp, nm], "ROOT")
        return None

    def VPPP(self, phrase):
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        pp = self.PP(phrase[:])
        if vp is not None and pp is not None:
            return Node([vp, pp], "ROOT")
        return None

    def VPprepP(self, phrase):
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        pp = self.prepP(phrase[:])
        if vp is not None and pp is not None:
            return Node([vp, pp], "ROOT")
        return None

    def VPNPprepP(self, phrase):
        vp_eles = []
        np_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        while len(phrase) > 0:
            if "prep" in phrase[0][1]:
                break
            np_eles.append(phrase.pop(0))
        vp = self.VP(vp_eles)
        np = self.NP(np_eles)
        pp = self.prepP(phrase[:])
        if vp is not None and np is not None and pp is not None:
            return Node([vp, np, pp], "ROOT")
        return None

    def VPp(self, phrase):
        last = phrase.pop()
        vp = self.VP(phrase[:])
        if vp is not None and "prep" in last[1]:
            return Node([vp, last[0]], "ROOT")

    def VPNPp(self, phrase):
        last = phrase.pop()
        vp_eles = []
        while len(phrase) > 0:
            vp_eles.append(phrase.pop(0))
            if self.isSomeVerb(vp_eles[-1][1]):
                break
        vp = self.VP(vp_eles)
        np = self.NP(phrase[:])
        if vp is not None and np is not None and "prep" in last[1]:
            return Node([vp, np, last[0]], "ROOT")
        return None

    def startsWithIsOrCan(self, phrase):
        if len(phrase) <= 1:
            return None
        if phrase[0][0] not in {"is", "can"}:
            return None
        first = phrase.pop(0)
        second = None
        if "ingV" in phrase[0][1] and first[0] == "is":
            if len(phrase) == 1:
                return Node([Node(["is", phrase[0][0]], "VP-ingV")], "ROOT")
            else:
                ing = phrase.pop(0)
                second = self.NP(phrase[:])
                if second is not None:
                    return Node([Node(["is", ing[0]], "VP-ingV"), second], "ROOT")
                second = self.prepP(phrase[:])
                if second is not None:
                    return Node([Node(["is", ing[0]], "VP-ingV"), second], "ROOT")
        if "baseV" in phrase[0][1] and first[0] == "can":
            if len(phrase) == 1:
                return Node([Node(["can", phrase[0][0]], "VP")], "ROOT")
            else:
                base = phrase.pop(0)
                second = self.NP(phrase[:])
                if second is not None:
                    return Node([Node(["can", base[0]], "VP"), second], "ROOT")
                second = self.prepP(phrase[:])
                if second is not None:
                    return Node([Node(["can", base[0]], "VP"), second], "ROOT")
        second = self.PP(phrase[:])
        if second is not None:
            return Node([Node([first[0]], "VP"), second], "ROOT")
        second = self.adjP(phrase[:])
        if second is not None:
            return Node([Node([first[0]], "VP"), second], "ROOT")
        second = self.NP(phrase[:])
        if second is not None:
            return Node([Node([first[0]], "VP"), second], "ROOT")
        second = self.NM(phrase[:])
        if second is not None:
            return Node([Node([first[0]], "VP"), second], "ROOT")
        return None
            
    def isSomeVerb(self, tags):
        return "baseV" in tags or "irV" in tags or "3PS" in tags
        
    def isSomeNoun(self, tags):
        return "noun" in tags or "plN" in tags or "quant" in tags or "pron" in tags