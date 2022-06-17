from fastapi import FastAPI
from fastapi.responses import StreamingResponse, Response
from enum import Enum
import uvicorn

import python_ast
import python_cfg

app = FastAPI()


class Format(str, Enum):
    png = 'image/png'
    svg = 'image/svg+xml'
    pdf = 'application/pdf'
    dot = 'text/dot'


example_code = """
a = 2 + 2 * (c * d / 2)
b = a + a / 2
if b > 4:
    print('hello')
else:
    print('nooo')
print('exit')
"""


@app.get('/python_ast', response_class=StreamingResponse)
def ast(format: Format, code: str = example_code):
    data = python_ast.make(code, format=format.name)
    return StreamingResponse(data, media_type=format.value)


@app.get('/python_cfg')
def cfg(code: str = example_code):
    data = python_cfg.make(code)
    return StreamingResponse(data, media_type=f"text/dot")


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True, debug=True)
