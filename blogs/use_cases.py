from pathlib import Path

from blogs.exceptions import BlogNotFound
from blogs.models import Blog, Post

BLOG_FILE = str(Path.cwd() / 'blogs_data' / 'blog_{}.json')


def create_new_post(blog_id: int, blog: Blog, post: Post):
    blog.posts.append(post)
    with open(BLOG_FILE.format(blog_id), 'w', encoding='utf-8') as file:
        file.write(blog.model_dump_json())


def load_blog(blog_id: int) -> Blog:
    try:
        with open(BLOG_FILE.format(blog_id), 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError as error:
        raise BlogNotFound() from error
    return Blog.model_validate_json(data)


def save_blog(blog_id: int, blog: Blog) -> None:
    with open(BLOG_FILE.format(blog_id), 'w', encoding='utf-8') as file:
        file.write(blog.model_dump_json())
