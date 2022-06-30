from kotlin.kotlin_ast import get_ast
from kotlin.kotlin_cfg import get_cfg


def handler(code: str, model: str):
    if model == 'ast':
        return get_ast(code)
    elif model == 'cfg':
        return get_cfg(code)
