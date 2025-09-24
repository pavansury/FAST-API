from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Tea(BaseModel):
    name: str
    id: str
    origin: str

test: list[Tea] = []

@app.get("/")
def read_root():
    return {"message": 'welcome to tea api'}

@app.get("/teas")
def teas():
    return test

@app.post("/teas")
def add_tea(tea: Tea):
    test.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(test):
        if tea.id == tea_id:
            test[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(test):
        if tea.id == tea_id:
            deleted_tea = test.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}