from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, Response, FileResponse
from fastapi.staticfiles import StaticFiles
from enum import Enum
import uvicorn

import python.python_ast as python_ast
import python.python_cfg as python_cfg

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

app = FastAPI()
app.mount("/client", StaticFiles(directory="../client"), name="client")


@app.get("/")
async def root(request: Request):
    return FileResponse('../client/views/index.html')


@app.get("/save")
async def save(request: Request):
    pass


@app.get('/python_ast', response_class=StreamingResponse)
async def ast(format: Format, code: str = example_code):
    data = python_ast.make(code, format=format.name)
    return StreamingResponse(data, media_type=format.value)


@app.get('/python_cfg')
async def cfg(code: str = example_code):    
    data = python_cfg.make(code)
    return StreamingResponse(data, media_type=f"text/dot")


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True, debug=True)
