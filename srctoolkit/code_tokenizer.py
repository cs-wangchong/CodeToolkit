#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import functools
import re
import requests

class CodeTokenizer:

    def __init__(self, searchcode_host="http://10.177.21.165:8080"):
        self.searchcode_api = searchcode_host + "/api/codesearch/?q={}&per_page=1"

    def split_camelcase(self, camel_case: str, to_lower=True):
        delimited_case = camel_case.replace('...', '-DOTDOTDOT-')
        delimited_case = delimited_case.split('.')[-1]
        delimited_case = delimited_case.replace('[]', ' []')
        delimited_case = delimited_case.replace('-DOTDOTDOT-', ' ...')
        delimited_case = re.sub(r'_', " ", delimited_case).strip()
        delimited_case = re.sub(
            r'([A-Za-z]| )([0-9]+)([A-Za-z]|$| )', r'\1 \2 \3', delimited_case)
        delimited_case = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', delimited_case)
        delimited_case = re.sub(r'([A-Z]+)', r' \1', delimited_case)
        delimited_case = re.sub(r'\s+', ' ', delimited_case)
        delimited_case = delimited_case.strip()

        if to_lower:
            delimited_case = delimited_case.lower()
        return delimited_case

    def word_count(self, word):
        url = self.searchcode_api.format(word)
        response = requests.get(url)
        count = response.json()['totalHits']
        print(f"count of '{word}': {count}")
        return count

    def handle_digit(self, words: list, min_hit=50) -> list:
        result = [words[0]]
        for current_word in words[1:]:
            previous_word = result[-1]
            if previous_word[-1].isdigit() or current_word[0].isdigit():
                potential = previous_word + current_word
                if self.word_count(potential) >= min_hit:
                    result.pop(-1)
                    current_word = f"{previous_word}{current_word}"
            result.append(current_word)
        return result

    def tokenize(self, identifier: str, min_hit=50):
        delimited_case = self.split_camelcase(identifier, to_lower=False)
        words = delimited_case.split()
        print("words after splitting camel case:", words)
        words = self.handle_digit(words, min_hit=min_hit)
        print("words after handling digits:", words)

        # TODO: handle other cases.
        # for example, split 'getinstance' into 'get' and 'instance'

        return words


if __name__ == "__main__":
    tokenizer = CodeTokenizer()
    tokenizer.tokenize("md5sum")
    tokenizer.tokenize("parseISO8601")
    tokenizer.tokenize("getPDFv2")