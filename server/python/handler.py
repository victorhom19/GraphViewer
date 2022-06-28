from python import python_ast, python_cfg


def handler(code: str, model: str):
    if model == 'ast':
        return python_ast.make(code)
    elif model == 'cfg':
        return python_cfg.make(code)
    pass
