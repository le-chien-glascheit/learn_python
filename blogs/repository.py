from blogs.models import Post

SEPARATOR = ';'


def save_post(post: Post) -> None:
    row = [post.title, post.text]
    bar = SEPARATOR.join(row)
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.write(bar + '\n')


def load_posts() -> list[Post]:
    with open('database.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    posts = []
    for line in lines:
        line_list = line.strip().split(SEPARATOR)
        post = Post(line_list[0], line_list[1])
        posts.append(post)
    return posts


if __name__ == '__main__':
    pass
    # post = Post('Just post', 'saved post')
    # save_post(post)
    # posts = load_posts()
    # print(*posts, sep='\n')
    # a = ['bobik', '2', 'dog']
    # b = '//'.join(a)
    # print(type(b))
    # print(b)
    # with open('database.txt', 'a', encoding='utf-8') as file:
    #     file.write(b + '\n')
    # with open('database.txt', 'r', encoding='utf-8') as file:
    #     lines = file.readlines()
    # data = []
    # for line in lines:
    #     data.append(line.strip().split('//'))
    # print(data)
