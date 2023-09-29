from http.client import responses

from fastapi import FastAPI, Body, Response
from fastapi.responses import FileResponse
import uvicorn

from system import Project

app = FastAPI()
app_project = Project()


@app.get("/")
def root():
    return FileResponse("templates/index.html")


@app.post("/first")
async def first(data=Body()):
    x = data["x"]
    y = data["y"]
    z = data["z"]
    status_code = Response().status_code
    message = responses[status_code]
    app_project.status_request(status_code, message)
    app_project.action(x, y, z)
    return app_project.id_show()


@app.get("/second")
async def second(value: int):
    for item in app_project.data_result:
        if value == item["id"]:
            return item["result"]


@app.get("/third")
async def third():
    return app_project.result()


if __name__ == "__main__":
    uvicorn.run(app)
