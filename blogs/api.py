import random
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from fastapi import FastAPI

from blogs.cli import blog
from blogs.use_cases import  create_new_post, print_posts
 #   from use_cases import print_posts, create_new_post
 #  ModuleNotFoundError: No module named 'use_cases'

app = FastAPI(
    title='Blog_api'
)


helloy = (f'HI,dear user на этом познания английского заканчиваються\nЕсли хотите создать пост допишите /create\nЕсли хотите посмотреть посты допешите /posts \n')
# странно но почему-то текст не начинаеться с новой строки... печаль


class Blog2(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    author: str = 'Василий'
    email: str = 'vasya@mail.ru'


@app.get('/')
def main_page() -> str:
    return helloy


@app.get('/create')
def create():
    create_new_post(
        blog=blog,
        title=input('title? >'),
        text=input('text? >'),
    )
    return ...


@app.get('/posts')
def posts():
    print_posts(blog)
    return ...

global_data = ''




def create():
    create_new_post(
        blog=blog,
        title=input('title? >'),
        text=input('text? >'),
    )
    return ...
@app.post(
    blog=blog,
    title ='Введите пожалуйста название вашего поста',
    text='Введите пожалуйста текст вашего поста',
)
def post_data(blog: Blog2) -> ...:
    return ...
# это одно и то же ?




#
# import random
# from uuid import UUID, uuid4
#
# from pydantic import BaseModel, Field
#
# from fastapi import FastAPI
#
# app = FastAPI(
#     title='MySuperAPI',
#     version='1.1.0'
# )
#
#
# @app.get('/')
# def main_page() -> int:
#     return random.randint(1, 15)
#
#
# @app.get('/test')
# def test_request() -> str:
#     return 'Hello, Api!'
#
#
# global_data = ''
#
#
# class CatOut(BaseModel):
#     id: UUID = Field(default_factory=uuid4)
#     name: str
#     age: float = 0
#
#
# class Cat(BaseModel):
#     name: str
#     age: float = 0
#
#
# @app.post(
#     path='/data',
#     name='Запостить дату',
#     description='С помощью этого метода вы можете отправить строку на сервер',
# )
# def post_data(cat: Cat) -> CatOut:
#     return CatOut.model_validate(cat, from_attributes=True)
#
#
# @app.get('/data')
# def post_data(s: int = 1) -> str:
#     return global_data[:-s]
