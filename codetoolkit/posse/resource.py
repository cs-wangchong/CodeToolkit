#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from pathlib import Path

DEFAULT_DICT_DIR = Path(__file__).parent / "dicts"
DEFAULT_DICT = {
}

DEFAULT_METHOD_CORPUS = Path(__file__).parent / "corpus/normal.methods"
DEFAULT_FIELD_CORPUS = Path(__file__).parent / "corpus/normal.fields"



def load_default_dict():
    with (DEFAULT_DICT_DIR /"dictionary-allwords").open("r", encoding="utf-8") as f:
        vocab = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["VOCAB"] = vocab
    with (DEFAULT_DICT_DIR /"preposition").open("r", encoding="utf-8") as f:
        prep = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["PREP"] = prep
    with (DEFAULT_DICT_DIR /"quant").open("r", encoding="utf-8") as f:
        quant = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["QUAN"] = quant
    with (DEFAULT_DICT_DIR /"irregV").open("r", encoding="utf-8") as f:
        irregV = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["IRRV"] = irregV
    with (DEFAULT_DICT_DIR /"adjective").open("r", encoding="utf-8") as f:
        adj = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["ADJ"] = adj
    with (DEFAULT_DICT_DIR /"adverb").open("r", encoding="utf-8") as f:
        adv = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["ADV"] = adv
    with (DEFAULT_DICT_DIR /"noun").open("r", encoding="utf-8") as f:
        noun = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["NOUN"] = noun
    with (DEFAULT_DICT_DIR /"verb").open("r", encoding="utf-8") as f:
        verb = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["VERB"] = verb
    with (DEFAULT_DICT_DIR /"pronoun").open("r", encoding="utf-8") as f:
        pronoun = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["PRON"] = pronoun
    with (DEFAULT_DICT_DIR /"n-abbr").open("r", encoding="utf-8") as f:
        nabbr = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["NABBR"] = nabbr
    with (DEFAULT_DICT_DIR /"participle").open("r", encoding="utf-8") as f:
        pp = {line.strip() for line in f if line.strip() != ""}
    DEFAULT_DICT["PP"] = pp


load_default_dict()


