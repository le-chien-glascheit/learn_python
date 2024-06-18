from fastapi import status

class BlogsError(Exception):
    status = status.HTTP_500_INTERNAL_SERVER_ERROR
    description = 'Неизвестная ошибка'


class BlogNotFound(BlogsError):
    status = status.HTTP_404_NOT_FOUND
    description = 'Блог не найден'


class AuthorInvalid(BlogsError):
    status = status.HTTP_400_BAD_REQUEST
    description = 'Обязательно автора или мыло'


