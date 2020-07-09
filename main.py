from fastapi import FastAPI
from enum import Enum

hello = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@hello.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}