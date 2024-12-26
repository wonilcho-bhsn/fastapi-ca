import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from user.interface.controller.user_controller import router as user_routers

# examples
from example.ch06_02.sync_ex import router as sync_ex_router
from example.ch06_02.async_ex import router as async_ex_router
from example.ch10_01.background_task import router as backgroundtasks_ex_router


app = FastAPI()
app.include_router(user_routers)
app.include_router(sync_ex_router)
app.include_router(async_ex_router)
app.include_router(backgroundtasks_ex_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request:Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )

@app.get("/")
def hello():
    return {"Hellow": "FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)