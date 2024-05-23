import click
SEPARATOR = ';'
import sys
from repository import save_post, load_posts
from models import Post, Blog
@click.command()
@click.argument('--title',help='Post title',type=Post)
@click.argument('--text',help='Post text',type=Post)


def create_new_post(blog: Blog):
    print('Создание нового поста')

    post = Post(title,text)
    save_post(post)
    blog.add_post(post)

def print_post(blog: Blog):
    print('Вывожу ваши посты')
    posts = blog.get_all_posts()
    print(*posts, sep='\n')

@click.command()
@click.argument()
def new():
    create_new_post(blog)

@click.command()
@click.argument()
def all():
    print_post(blog)

@click.command()
@click.argument()
def exit():
    print('Выход')
    sys.exit()


@click.command()
@click.argument()
def help():
    print('new - Создание нового поста')
    print('all - Вывод всех ваших постов')
    print('exit - Выход')
    print('help - Вывод команд')


@click.group()
def main():
   pass



if __name__ == '__main__':
    main()