from pathlib import Path

class VerbHelper:
    __INSTANCE = None
    VERB_TENSES_KEYS = {
        "infinitive"           : 0,
        "1st singular present" : 1,
        "2nd singular present" : 2,
        "3rd singular present" : 3,
        "present plural"       : 4,
        "present participle"   : 5,
        "1st singular past"    : 6,
        "2nd singular past"    : 7,
        "3rd singular past"    : 8,
        "past plural"          : 9,
        "past"                 : 10,
        "past participle"      : 11
    }

    VERB_TENSES_ALIASES = {
        "inf"     : "infinitive",
        "1sgpres" : "1st singular present",
        "2sgpres" : "2nd singular present",
        "3sgpres" : "3rd singular present",
        "pl"      : "present plural",
        "prog"    : "present participle",
        "1sgpast" : "1st singular past",
        "2sgpast" : "2nd singular past",
        "3sgpast" : "3rd singular past",
        "pastpl"  : "past plural",
        "ppart"   : "past participle"
    }

    def __init__(self, dictionary=str(Path(__file__).parent / "verb.txt")):
        self.verb_tenses = {}
        with Path(dictionary).open("r", encoding="utf-8") as f:
            for line in f:
                strs = line.strip().split(",")
                self.verb_tenses[strs[0]] = strs

        self.verb_lemmas = {}
        for infinitive in self.verb_tenses:
            for tense in self.verb_tenses[infinitive]:
                if tense != "":
                    self.verb_lemmas[tense] = infinitive

    @classmethod
    def get_inst(cls, *args):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls(*args)
        return cls.__INSTANCE

    def verb_conjugate(self, verb, tense="infinitive", negate=False):
        """Inflects the verb to the given tense.
        For example: be
        present: I am, you are, she is,
        present participle: being,
        past: I was, you were, he was,
        past participle: been,
        negated present: I am not, you aren't, it isn't.
        """
        _verb = self.verb_lemmas.get(verb, "")
        i = VerbHelper.VERB_TENSES_KEYS[tense]
        if negate is True: 
            i += len(VerbHelper.VERB_TENSES_KEYS)
        if _verb not in self.verb_tenses:
            return verb
        return self.verb_tenses[_verb][i]

    def verb_past(self, verb, negate=False):
        elements = verb.split()
        _verb = elements[-1]
        
        if _verb not in self.verb_lemmas:
            if _verb.endswith("e"):
                _verb = f"{_verb}d"
            else:
                _verb = f"{_verb}ed"
            adv = elements[:-1]
            return " ".join(adv + [_verb])

        _verb = self.verb_lemmas[_verb]
        index = VerbHelper.VERB_TENSES_KEYS["past"]
        if negate is True: 
            index += len(VerbHelper.VERB_TENSES_KEYS)

        if _verb not in self.verb_tenses or self.verb_tenses[_verb][index] == "":
            if _verb.endswith("e"):
                _verb = f"{_verb}d"
            else:
                _verb = f"{_verb}ed"
            adv = elements[:-1]
            return " ".join(adv + [_verb])

        return " ".join(elements[:-1] + [self.verb_tenses[_verb][index]])