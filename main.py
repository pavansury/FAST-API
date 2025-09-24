from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Tea(BaseModel):
    name: str
    id: str
    origin: str

test: list[Tea] = []


