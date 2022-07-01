from java.java_ast import get_ast


def handler(code: str, model: str):
    if model == 'ast':
        return get_ast(code)
