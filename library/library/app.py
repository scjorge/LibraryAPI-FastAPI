from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Hello World
    """

    return {"message": "hello world"}
