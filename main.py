from fastapi import FastAPI
from study.useApi.agriFoodAPI import FoodNutrition
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/nutrition")
async def get_nutrition(key: str, food_group_code: str, food_name: str):
    return {"response": FoodNutrition().find_food_nutrition(key, food_group_code, food_name)}
