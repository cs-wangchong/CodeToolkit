#!/usr/bin/env python
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    from codetoolkit.code_pos import CodePOS

    codepos = CodePOS.get_inst()
    for word, tag in codepos("add item to index"):
        print(word, "|", tag)