#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from codetoolkit.javalang.parse import parse
from codetoolkit.javalang.tree import StatementExpression

if __name__ == "__main__":
    for _, node in parse(open("test/Sample1.java").read()).filter(StatementExpression):
        print(node)