import uvicorn
from fastapi import FastAPI

from user.interface.controller.user_controller import router as user_routers

app = FastAPI()
app.include_router(user_routers)

@app.get("/")
def hello():
    return {"Hellow": "FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)