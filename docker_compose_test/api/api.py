from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/")
async def home():
    return "api : 8080"


@app.post("/hi")
async def say_hi():
    return "hi api : 8080"
