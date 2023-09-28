
from fastapi import FastAPI, Body, BackgroundTasks
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


def actions(x, y, z):
    if z == "+":
        return {"message": f"{x + y}"}
    elif z == "-":
        return {"message": f"{x - y}"}
    elif z == "*":
        return {"message": f"{x * y}"}
    elif z == "/":
        return {"message": f"{x / y}"}


@app.get("/")
def root():
    return FileResponse("templates/index.html")


@app.post("/first")
async def first(background_tasks: BackgroundTasks, data=Body()):
    x = data["x"]
    y = data["y"]
    z = data["z"]
    # background_tasks.add_task(data, )
    return actions(x, y, z)


if __name__ == "__main__":
    uvicorn.run(app)
