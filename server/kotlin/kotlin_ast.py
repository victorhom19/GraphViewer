import re

from antlr4 import *
from antlr4.tree.Trees import Trees

from server.kotlin.antlr.KotlinLexer import KotlinLexer
from server.kotlin.antlr.KotlinParser import KotlinParser
from server.kotlin.dot_gen.get_dot import get_dot


def get_ast(code):
    inp_stream = InputStream(code)
    lexer = KotlinLexer(inp_stream)
    stream = CommonTokenStream(lexer)
    parser = KotlinParser(stream)
    tree = parser.kotlinFile()
    str_tree = Trees.toStringTree(tree, None, parser)
    reg = re.compile(r'(\s\(\s*\))|\\n')
    sub = reg.sub('', str_tree)
    sub = sub.replace('"', '\\"')
    print(sub)
    return get_dot(sub)
