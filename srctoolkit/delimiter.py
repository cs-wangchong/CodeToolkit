#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import functools
import re

from .spiral import ronin

class Delimiter:

    # @staticmethod
    # @functools.lru_cache(maxsize=10000)
    # def split_camel(camel_case: str, to_lower=True):
    #     delimited_case = camel_case.replace('...', '-DOTDOTDOT-')
    #     delimited_case = delimited_case.split('.')[-1]
    #     delimited_case = delimited_case.replace('[]', ' []')
    #     delimited_case = delimited_case.replace('-DOTDOTDOT-', ' ...')
    #     delimited_case = re.sub(r'_', " ", delimited_case).strip()
    #     delimited_case = re.sub(
    #         r'([A-Za-z]| )([0-9]+)([A-Za-z]|$| )', r'\1 \2 \3', delimited_case)
    #     delimited_case = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', delimited_case)
    #     delimited_case = re.sub(r'([A-Z]+)', r' \1', delimited_case)
    #     delimited_case = re.sub(r'\s+', ' ', delimited_case)
    #     delimited_case = delimited_case.strip()

    #     if to_lower:
    #         delimited_case = delimited_case.lower()
    #     return delimited_case

    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def split_camel(camel_case: str, to_lower=True):
        delimited_result: list = ronin.split(camel_case)
        # check ['...']
        if camel_case.endswith('...'): delimited_result.append('...')
        # check ['mult', 'i']
        size = len(delimited_result)
        for i in range(size):
            if i < size - 1 and delimited_result[i]=='mult' and delimited_result[i+1]=='i':
                pre = delimited_result[:i]
                pre.append('multi')
                pre.extend(delimited_result[i+2:])
                delimited_result = pre
                break
        delimited_case = ' '.join(delimited_result)
        
        if to_lower:
            delimited_case = delimited_case.lower()
        return delimited_case