from blogs.use_cases import create_new_post, print_posts, save_blog
from blogs.models import Blog, Post


if __name__ == '__main__':

    post1 = Post(title ='Самый первый пост',
                 text = 'Сегодня вымешленный персонаж рассказыват о себе'
                        )
    post2 = Post(title='Второй пост',
                 text='Сегодня вымешленный персонаж поведает вам о своей собаке'
                        )
    post3 = Post(title='Самый первый пост',
                 text='Сегодня вымешленный персонаж рассказыват о себе'
                        )

    blog = Blog(
        author='Vlad',
        email='vlad@gaz.ru',
        posts=[post1, post2, post3]
    )

    save_blog(blog)
    # print_posts()
    blog = Blog.model_validate_json(data)

# create_new_post(
#     blog,
#     post=Post(title='Второй пост', text='Сегодня вымешленный персонаж поведает вам о своей собаке'
#                 )
# )
