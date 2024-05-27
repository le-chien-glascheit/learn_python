import sys

from use_cases import create_new_post, print_posts
from repository import load_posts
from models import Blog


def main():
    print('Инициализация программы (загрузка данных с диска)')

    blog = Blog(author='Vlad', email='vlad@gaz.ru')
    for post in load_posts():
        blog.add_post(post)

    print('Дарова,', blog.author)
    while True:
        command = input('command> ')
        match command.lower():
            case 'new':
                create_new_post(
                    blog=blog,
                    title=input('title? >'),
                    text=input('text? >'),
                )
            case 'all':
                print_posts(blog)
            case 'exit':
                print('Выход')
                sys.exit()
            case 'help':
                print('new - Создание нового поста')
                print('all - Вывод всех ваших постов')
                print('exit - Выход')
                print('help - Вывод команд')
            case _:
                print('Неизвестная команда')


if __name__ == '__main__':
    main()
