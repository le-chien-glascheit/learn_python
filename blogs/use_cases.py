from blogs.models import Blog, Post
from blogs.repository import save_post


def create_new_post(blog: Blog, title: str, text: str):
    post = Post(title=title, text=text)
    save_post(post)
    blog.add_post(post)


def print_posts(blog: Blog):
    print('Вывожу ваши посты')
    posts = blog.get_all_posts()
    print(*posts, sep='\n')
