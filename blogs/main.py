import sys

from repository import save_post, load_posts
from models import Post, Blog


def create_new_post(blog: Blog):
    print('Создание нового поста')

    post = Post(
        title=input('Название >'),
        text=input('Текст >'),
    )
    save_post(post)
    blog.add_post(post)


def print_post(blog: Blog):
    print('Вывожу ваши посты')
    posts = blog.get_all_posts()
    print(*posts, sep='\n')


def main():
    print('Инициализация программы (загрузка данных с диска)')

    blog = Blog(author='Vlad', email='vlad@gaz.ru')
    posts = load_posts()
    for post in posts:
        blog.add_post(post)

    print('Дарова,', blog.author)
    while True:
        command = input('command> ')
        match command.lower():
            case 'new':
                create_new_post(blog)
            case 'all':
                print_post(blog)
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
