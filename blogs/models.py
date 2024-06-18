from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    text: str


class Blog(BaseModel):
    author: str
    email: EmailStr
    posts: list[Post]


