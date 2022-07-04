from java.java_ast import get_ast

from java.java_cfg import get_cfg


def handler(code: str, model: str):
    if model == 'ast':
        return get_ast(code)
    else:
        return get_cfg(code)
