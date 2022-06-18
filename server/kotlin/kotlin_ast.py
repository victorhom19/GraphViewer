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
    get_dot(tree)
    print(Trees.toStringTree(tree, None, parser))
