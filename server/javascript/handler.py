from javascript.ast import js_ast
from javascript.cfg import js_cfg


def handler(code: str, model: str):
    if model == 'ast':
        return js_ast.make(code)
    if model == 'cfg':
        return js_cfg.make(code)
