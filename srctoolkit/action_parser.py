#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import itertools

from .javalang.parse import parse as ast_parse
from .javalang.tokenizer import Literal
from .javalang.tree import CompilationUnit, ClassDeclaration, FieldDeclaration, MemberReference, MethodDeclaration, MethodInvocation
from .delimiter import Delimiter
from .code_pos import CodePOS
from .code_chunker import CodeChunker
from .lemmatizer import Lemmatizer
from .dictionary import PREPOSITIONS


class ActionParser:
    __INSTANCE = None

    def __init__(
        self,
        code_pos=CodePOS.get_inst(),
        code_chunker=CodeChunker.get_inst(),
    ):
        self.code_pos = code_pos
        self.code_chunker = code_chunker

    @classmethod
    def get_inst(cls, *args):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls()
        return cls.__INSTANCE


    def __call__(self, *args):
        return self.parse(*args)

    def parse_method_declaration(self, clazz_name, method_name, params, ret):
        verb2nameroles = self.parse_method_name(method_name, ret)
        verb2roles = self.complete_role(verb2nameroles, clazz_name, params)
        return verb2roles

    def parse_method_name(self, name, ret):
        segmented_name = Delimiter.split_camel(name)
        pos = self.code_pos(segmented_name)
        verbs = {word for word, tag in pos if tag ==
                 "verb" and not word.endswith("ed") and not word.endswith("ing")}
        verb2chunks = self.code_chunker(segmented_name, *verbs)

        verb2nameroles = {}
        for verb, chunks in verb2chunks.items():
            if verb is None:
                continue
            lemma = Lemmatizer.lemmatize_verb(verb)
            name_role = []
            verb_index = -1
            prep_indices = []
            for index, chunk in enumerate(chunks):
                if chunk == verb:
                    verb_index = index
                elif chunk in PREPOSITIONS and verb_index >= 0 and index > verb_index:
                    prep_indices.append(index)
            if verb_index > 0:
                prefix = " ".join(chunks[:verb_index])
                if ret.lower() == "boolean":
                    name_role.append((prefix, "subj"))
                else:
                    # name_role.append((prefix, "advmod"))
                    verb = f"{prefix} {verb}"
            name_role.append((verb, "verb"))

            if len(prep_indices) > 0:
                if prep_indices[0] > verb_index + 1:
                    dobj = " ".join(chunks[verb_index + 1:prep_indices[0]])
                    name_role.append((dobj, "dobj"))
                for start, end in zip(prep_indices, prep_indices[1:] + [len(chunks)]):
                    prep = chunks[start]
                    name_role.append((prep, "prep"))
                    if start + 1 < end:
                        pobj = " ".join(chunks[start + 1:end])
                        name_role.append((pobj, "pobj"))
                    else:
                        pobj = None
                    # iobj.append((prep, pobj))
            else:
                if verb_index + 1 < len(chunks):
                    dobj = " ".join(chunks[verb_index + 1:])
                    name_role.append((dobj, "dobj"))
            verb2nameroles[verb] = name_role
        return verb2nameroles

    def complete_role(self, verb2nameroles: dict, clazz_name, params):
        verb2roles = dict()
        segmented_clazz = Delimiter.split_camel(clazz_name)
        for verb, name_roles in verb2nameroles.items():
            name_nps = {phrase for phrase,
                        role in name_roles if role not in {"verb", "prep"}}
            params = [Delimiter.split_camel(param) for param in params]
            params = [param for param in params if param not in name_nps]
            size = len(name_roles)

            phrases, roles = [], []
            for index, (phrase, role) in enumerate(name_roles):
                phrases.append(phrase)
                roles.append(role)
                if role == "verb":
                    if index + 1 < size and name_roles[index + 1][1] == "prep":
                        phrases.append(segmented_clazz)
                        roles.append("dobj")
                    elif index + 1 == size:
                        if len(params) > 0:
                            phrases.append(params.pop(0))
                            roles.append("dobj")
                        else:
                            phrases.append(segmented_clazz)
                            roles.append("dobj")
                elif role == "prep" and index + 1 < size and name_roles[index + 1][1] != "pobj" and len(params) > 0:
                    phrases.append(params.pop(0))
                    roles.append("pobj")

            if len(roles) > 0 and roles[-1] == "prep" and len(params) > 0:
                phrases.append(params.pop(0))
                roles.append("pobj")

            # if len(roles) > 0 and roles[-1] != "pobj":
            #     lemma = Lemmatizer.lemmatize_verb(verb)
            #     preps = VERB_PATTERN.get(lemma, [])

            #     # TODO: improve this part
            #     if len(preps) > 0:
            #         prep = preps[0]
            #         if len(params) > 0:
            #             phrases.append(prep)
            #             roles.append("prep")
            #             phrases.append(params.pop(0))
            #             roles.append("pobj")
            #         else:
            #             phrases.append(prep)
            #             roles.append("prep")
            #             phrases.append(segmented_clazz)
            #             roles.append("pobj")

            subj = None
            dobj = None
            iobj = []
            size = len(phrases)
            index = 0
            while index < size:
                phrase = phrases[index]
                role_type = roles[index]
                if role_type == "subj":
                    subj = phrase
                elif role_type == "dobj":
                    dobj = phrase
                elif role_type == "prep" and index + 1 < size:
                    iobj.append((phrase, phrases[index + 1]))
                    index += 1
                index += 1

            verb2roles[verb] = dict()
            if subj is not None:
                verb2roles[verb]["subj"] = subj
            verb2roles[verb]["verb"] = verb
            if dobj is not None:
                verb2roles[verb]["dobj"] = dobj
            if len(iobj) > 0:
                verb2roles[verb]["iobj"] = iobj
        return verb2roles

    #处理参数中的MethodInvocation
    def deal_invocation(self, methodInvocation):
        scope = str(methodInvocation.qualifier)
        invoke_method = str(methodInvocation.member)
        arguments = methodInvocation.arguments
        arg_list = list()
        for arg in arguments:
            if isinstance(arg, MemberReference):
                if arg.qualifier is None:
                    arg_list.append(str(arg.member))
                else:
                    arg_list.append(arg.qualifier + arg.member)
            if isinstance(arg, Literal):
                arg_list.append(arg.value)
            if isinstance(arg, MethodInvocation):
                arg_list.append(self.deal_invocation(arg))
        str_invocation = scope.join(".").join(invoke_method).join("(")
        for item in arg_list:
            str_invocation.join(item)
        str_invocation.join(")")
        return str_invocation

    #把生成的主谓宾组成三元组
    def convert_to_triples(self, action, method_name : str):
        desc = list()
        for key in action.keys():
            content = action[key]
            #subj不存在则把方法名当作subj
            if 'subj' in content:
                subj = content['subj']
            else:
                subj = method_name

            verb = content['verb']
            dobj = content['dobj']
            
            if 'iobj' in content:
                iobjs = content['iobj']
            else:
                iobjs = None

            sub_desc = (subj, verb, dobj)
            desc.append(sub_desc)
            if iobjs is not None:
                for iobj in iobjs:
                    temp = str("")
                    for word in iobj:
                        temp = temp + str(word) + " "
                    temp = temp[:-1]
                    sub_desc = (subj, verb, temp)
                    desc.append(sub_desc)
        return desc

    #提取代码中的方法调用，并且生成相应的句子成分
    def parse(self, code):
        if isinstance(code, CompilationUnit):
            tree = code
        else:
            try:
                tree = ast_parse(code)
            except Exception:
                return []
        clazz_decl = (tree.types)[0]
        clazz_name = clazz_decl.name
        #获取class中的method
        for node in clazz_decl.body:
            if isinstance(node, MethodDeclaration):
                method_decl = node
        #获取method的返回值
        if method_decl.return_type is None:
            ret = "void"
        else:
            ret = method_decl.return_type

        method_params = list()
        for param in method_decl.parameters:
            method_params.append(param.type.name)
            method_params.append(param.name)
        #主谓宾结果集
        results = list()

        #首先将方法声明主谓宾加入结果集
        action = self.parse_method_declaration(clazz_name, method_decl.name, method_params, ret)
        result = self.convert_to_triples(action, method_decl.name)[0]
        results.append(result)
        #获取method中的MethodInvocation，并生成相应主谓宾加入结果集
        for _, node in method_decl:
            if isinstance(node, MethodInvocation):
                scope = node.qualifier
                invoke_method = node.member
                invoke_arguments = list()
                for arg in node.arguments:
                    if isinstance(arg, MemberReference):
                        if arg.qualifier is None:
                            invoke_arguments.append(str(arg.member))
                        else:
                            invoke_arguments.append(arg.qualifier + arg.member)
                    if isinstance(arg, MethodInvocation):
                        invoke_arguments.append(self.deal_invocation(arg))                        
                    if isinstance(arg, Literal):
                        invoke_arguments.append(str(arg.value))
                action = self.parse_method_declaration(scope, invoke_method, invoke_arguments, ret)
                desc = self.convert_to_triples(action, invoke_method)
                if len(desc) > 1:
                    for item in desc:
                        results.append(item)
                else:
                    results.append(desc[0])
        return results