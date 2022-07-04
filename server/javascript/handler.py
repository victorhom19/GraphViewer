from javascript.ast import js_ast


def handler(code: str, model: str):
    if model == 'ast':
        return js_ast.make(code)
