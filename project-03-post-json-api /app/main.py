from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EchoRequest(BaseModel):
    message: str


@app.post("/echo")
def echo_message(request: EchoRequest):
    return {
        "message": request.message
    }