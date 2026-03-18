from fastapi import FastAPI

app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
