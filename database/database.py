from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.article import Article

admin_collection = Admin
article_collection = Article

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
