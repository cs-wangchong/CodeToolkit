#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import re
from .javalang.tokenizer import JavaToken
from typing import List


class CodeCleaner:
    @staticmethod
    def clean_annotation(tokens:List[JavaToken]):
        cleaned_tokens = []
        size = len(tokens)
        index = 0
        flag = False
        left = 0
        right = 0
        while index < size:
            token = tokens[index]
            index += 1
            if len(token.value) == 0:
                continue
            if token.value == "@":
                flag = True
                index += 1
                continue
            if flag:
                if token.value == "(":
                    left += 1
                elif token.value == ")":
                    right += 1
                elif left == right:
                    flag = False
            if not flag:
                cleaned_tokens.append(token)
        return cleaned_tokens
            