from blogs.models import Blog, Post
from blogs.repository import save_post


def create_new_post(blog: Blog, post: Post):
    blog.posts.append(post)
    with open('Post_data.json', 'w', encoding='utf-8') as file:
        file.write(blog.model_dump_json())



# def print_posts() -> Blog:
#     with open('Post_data.json', 'r', encoding='utf-8') as file:
#         data = file.read()
#     blog = Blog.model_validate_json(data)
#     return blog

def load_blog() -> Blog:
    with open('Post_data.json', 'r', encoding='utf-8') as file:
        data = file.read()
    blog = Blog.model_validate_json(data)
    return blog

def save_blog(blog: Blog)  -> None:
    with open('Post_data.json', 'w', encoding='utf-8') as file:
        file.write(blog.model_dump_json())
