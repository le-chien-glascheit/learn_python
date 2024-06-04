from pydantic import BaseModel, EmailStr
from pprint import pprint


class Post(BaseModel):
    title: str
    text: str


class Blog(BaseModel):
    author: str
    email: EmailStr
    posts: list[Post]


def read_data() -> Blog:
    with open('blog.json', 'r', encoding='utf-8') as file:
        data = file.read()
    blog = Blog.model_validate_json(data)
    return blog


def write_data():
    post = Post(title='Title1', text='Some text')
    post2 = Post(title='Title2', text='Some text')
    blog = Blog(
        author='Ivan',
        email='ivan@gmail.com',
        posts=[post, post2]
    )
    post3 = Post(title='Title3', text='Some text')
    blog.posts.append(post3)
    with open('blog.json', 'w', encoding='utf-8') as file:
        file.write(blog.model_dump_json())
