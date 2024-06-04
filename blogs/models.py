from dataclasses import dataclass
# from pydantic import BaseModel, EmailStr
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr
# from blogs.use_cases import create_new_post, print_posts


class Post(BaseModel):
    title: str
    text: str


class Blog(BaseModel):
    author: str
    email: EmailStr
    posts: list[Post]



if __name__ == '__main__':
    pass
    # blog = Blog(author='Vlad', email='vlad@gaz.ru')
    #
    # create_new_post(
    #     blog,
    #     post = Post(title ='Самый первый пост', text = 'Сегодня вымешленный персонаж рассказыват о себе'
    #                 )
    # )
    #
    #










#     def add_post(self, post: Post):
#         self.posts.append(post)
#
#
# def add_post(post: Post) -> None:
#     blog.posts.append(post)
#     with open('Post_data.json', 'w', encoding='utf-8') as file:
#         file.write(blog.model_dump_json())
#     # self._posts.append(post)
#
#
#     blog.posts.append = add_post
#
# def get_all_posts() -> Blog:
#     with open('Post_data.json', 'r', encoding='utf-8') as file:
#         data = file.read()
#     blog = Blog.model_validate_json(data)
#     return blog
#
