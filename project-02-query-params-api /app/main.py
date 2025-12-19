from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }