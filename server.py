import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
async def root(request: Request):
    return FileResponse('client/views/index.html')


@app.get("/save")
async def save(request: Request):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
