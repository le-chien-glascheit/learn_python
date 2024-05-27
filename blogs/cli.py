import click

from use_cases import print_posts, create_new_post
from repository import load_posts
from models import Blog


SEPARATOR = ';'

blog = Blog(author='Me', email='my@remail.com')
for post in load_posts():
    blog.add_post(post)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--title', '-T', required=True, help='Заголовок поста')
@click.option('--text', '-t', required=True)
def new(title, text):
    """Создаёт новый пост"""
    click.secho('Создание нового поста')
    create_new_post(blog=blog, title=title, text=text)


@cli.command()
def all():
    print_posts(blog=blog)


if __name__ == '__main__':
    cli()
