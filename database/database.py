from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.student import Student
from models.article import Article

admin_collection = Admin
article_collection = Article
student_collection = Student

# ADMIN
async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


# ARTICLE
async def retrieve_articles() -> List[Article]:
    articles = await article_collection.all().to_list()
    return articles


async def retrieve_article(id: PydanticObjectId) -> Article:
    article = await article_collection.get(id)
    if article:
        return article


async def add_article(new_article: Article) -> Article:
    article = await new_article.create()
    return article


async def delete_article(id: PydanticObjectId) -> bool:
    article = await article_collection.get(id)
    if article:
        await article.delete()
        return True


async def update_article_data(id: PydanticObjectId, data: dict) -> Union[bool, Article]:
    article_data = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in article_data.items()
    }}
    article = await article_collection.get(id)
    if article:
        await article.update(update_query)
        return article
    return False


# STUDENTS
# async def retrieve_students() -> List[Student]:
#     students = await student_collection.all().to_list()
#     return students


# async def add_student(new_student: Student) -> Student:
#     student = await new_student.create()
#     return student


# async def retrieve_student(id: PydanticObjectId) -> Student:
#     student = await student_collection.get(id)
#     if student:
#         return student


# async def delete_student(id: PydanticObjectId) -> bool:
#     student = await student_collection.get(id)
#     if student:
#         await student.delete()
#         return True


# async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
#     des_body = {k: v for k, v in data.items() if v is not None}
#     update_query = {"$set": {
#         field: value for field, value in des_body.items()
#     }}
#     student = await student_collection.get(id)
#     if student:
#         await student.update(update_query)
#         return student
#     return False
