from contextlib import contextmanager, asynccontextmanager
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from blogs.models import Blog
from blogs.use_cases import create_new_post, print_posts, load_blog

hello = """
HI,dear user на этом познания английского заканчиваються

Если хотите создать пост допишите /create

Если хотите посмотреть посты допешите /posts
"""


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    global blog
    blog = load_blog()
    yield


app = FastAPI(
    title='Blog_api',
    lifespan=lifespan,
    description=hello,
)

blog = Blog(author='Ivan', email='Ivan@ivanov.com')


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


@app.post('/post')
def create(post: Post) -> None:
    create_new_post(
        blog=blog,
        title=post.title,
        text=post.text,
    )


@app.get('/post')
def get_posts() -> list[Post]:
    return [
        Post.model_validate(post, from_attributes=True)
        for post in blog.get_all_posts()
    ]


@app.get('/blog')
def get_blog() -> BlogOut:
    return BlogOut.model_validate(blog, from_attributes=True)


@app.put('/blog')
def put_blog(new_blog: BlogIn) -> BlogOut:
    global blog
    blog = new_blog
    return BlogOut.model_validate(blog, from_attributes=True)


@app.patch('/blog')
def update_blog(
        author: str | None = None,
        email: str | None = None,
) -> None:
    if author is not None:
        blog.author = author
    if email is not None:
        blog.email = email
    if author is None and email is None:
        raise HTTPException(
            status_code=400,
            detail='Обязательно автора или мыло'
        )
