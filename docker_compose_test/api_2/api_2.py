from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/")
async def home():
    return "api2 : 9210"


@app.post("/hi")
async def say_hi():
    return "hi api2 : 9210"
