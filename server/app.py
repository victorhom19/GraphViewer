from enum import Enum

import uvicorn
from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from server.python import python_ast, python_cfg
from server.python.handler import handler as py_handler
from server.kotlin.handler import handler as kt_handler
import server.c.handler as c_handler

app = FastAPI()

functions = ["pythonast", "pythoncfg", "kotlinast"]
handlers = {"python": py_handler, "kotlin": kt_handler}


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


@app.get('/viewgraph')                                   # Not tested!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
async def cfg(code: str = example_code, lang: str = "python", model: str = "ast"):
    if (lang + model) in functions:
        data = handlers.get(lang)(code, model)
        return StreamingResponse(data, media_type=f"text/dot")


@app.get('/c_ssa', response_class=Response)
async def c_ssa(code: str = c_handler.example_code):
    try:
        data = c_handler.handler(code, model='ssa')
    except RuntimeError as e:
        raise HTTPException(400, detail=str(e))
    return Response(data, media_type=f"text/dot")


@app.get('/c_cfg', response_class=Response)
async def c_cfg(code: str = c_handler.example_code):
    try:
        data = c_handler.handler(code, model='cfg')
    except RuntimeError as e:
        raise HTTPException(400, detail=str(e))
    return Response(data, media_type=f"text/dot")


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True, debug=True)
