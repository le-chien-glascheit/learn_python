import random
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from fastapi import FastAPI

app = FastAPI(
    title='MySuperAPI',
    version='1.1.0'
)


@app.get('/')
def main_page() -> int:
    return random.randint(1, 15)


@app.get('/test')
def test_request() -> str:
    return 'Hello, Api!'


global_data = ''


class CatOut(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    age: float = 0


class Cat(BaseModel):
    name: str
    age: float = 0


@app.post(
    path='/data',
    name='Запостить дату',
    description='С помощью этого метода вы можете отправить строку на сервер',
)
def post_data(cat: Cat) -> CatOut:
    return CatOut.model_validate(cat, from_attributes=True)


@app.get('/data')
def post_data(s: int = 1) -> str:
    return global_data[:-s]
