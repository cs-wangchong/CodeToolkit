#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from srctoolkit.javalang.parse import parse
from srctoolkit.javalang.tree import StatementExpression

if __name__ == "__main__":
    code = '''
    public class A {public static void wait ( JSONRPC self ) {
  @ ParamToProperty ( action = "idle" ) @ ParamToProperty ( action = "update" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty ( action = "timeout" ) @ ParamToProperty ( action = "package" ) @ ParamToProperty (}
    '''
    for _, node in parse(code).filter(StatementExpression):
        print(node)