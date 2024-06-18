import os
from pathlib import Path

from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.requests import Request

from blogs.exceptions import BlogsError, AuthorInvalid
from blogs.models import Blog
from blogs.use_cases import create_new_post, load_blog

hello = """
HI,dear user на этом познания английского заканчиваються

Если хотите создать пост допишите /create

Если хотите посмотреть посты допешите /posts
"""


app = FastAPI(
    title='Blog_api',
    description=hello,
)

blog = Blog(author='Ivan', email='Ivan@ivanov.com', posts=[])


class Post(BaseModel):
    title: str
    text: str


class BlogOut(BaseModel):

    author: str
    email: EmailStr | None


class BlogIn(BlogOut):
    pass


@app.get('/')
def main_page() -> RedirectResponse:
    return RedirectResponse('/docs')


@app.get('/test/{path_param}/id/{path_id}')
def param_demo(
        path_param: str,
        path_id: str,
        page: str,
        query_id: int = 15,
) -> dict:
    return dict(
        a=path_param,
        b=path_id,
        c=page,
        d=query_id,
    )


@app.post('/blog/{blog_id}/post')
def create(blog_id: int, post: Post) -> None:
    # with open(BLOG_FILE.format(blog_id), 'r', encoding='utf-8') as file:
    #     data = file.read()
    load_blog(blog_id)
    create_new_post(
        blog_id=blog_id,
        blog=blog,
        post=post
    )


@app.get('/post/{blog_id}')
def get_posts(blog_id: int) -> list[Post]:
    load_blog(blog_id)
    return [
        Post.model_validate(post, from_attributes=True)
        for post in blog.posts
    ]


@app.get('/blog/{blog_id}')
# def param_demo(path_id: int) -> dict:
#     return dict(id=path_id)
def get_blog(blog_id: int) -> BlogOut:
    load_blog(blog_id)
    return BlogOut.model_validate(blog, from_attributes=True)


@app.put('/blog/{blog_id}')
def put_blog(blog_id: int, new_blog: BlogIn) -> BlogOut:
    load_blog(blog_id)
    blog = new_blog
    return BlogOut.model_validate(blog, from_attributes=True)


@app.patch('/blog/{blog_id}/')
def update_blog(
        blog_id: int,
        author: str | None = None,
        email: EmailStr | None = None,
) -> None:
    load_blog(blog_id)

    if author is not None:
        blog.author = author
    if email is not None:
        blog.email = email
    if author is None and email is None:
        raise AuthorInvalid



@app.exception_handler(BlogsError)
def handle_file_not_found_error(request: Request, exception: BlogsError):
    raise HTTPException(
        status_code=exception.status,
        detail=exception.description
    )

@app.get('/blog')
def hgs():
    print(os.listdir(Path.cwd() / 'blogs_data'))




















