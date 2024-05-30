from dataclasses import dataclass


@dataclass
class Post:
    title: str
    text: str


class Blog:
    def __init__(
            self,
            author: str,
            email: str,
    ):
        self.author = author
        self.email = email
        self._posts = []

    def add_post(self, post: Post):
        self._posts.append(post)

    def get_all_posts(self):
        return self._posts


if __name__ == '__main__':
    blog = Blog(author='Vlad', email='vlad@gaz.ru')
    while True:
        post = Post(
            title=input('Название >'),
            text=input('Текст >'),
        )
        blog.add_post(post)
        for index, post in enumerate(blog.get_all_posts()):
            print(f'Пост {index + 1}: {post}')
