from fastapi import APIRouter, Body

from database.database import *
from models.article import *

router = APIRouter()


@router.get("", response_description="Articles retrieved", response_model=Response)
async def get_articles():
    articles = await retrieve_articles()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Articles data retrieved successfully",
        "data": articles
    }


@router.get("/{id}", response_description="Article data retrieved", response_model=Response)
async def get_article(id: PydanticObjectId):
    article = await retrieve_article(id)
    if article:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Article data retrieved successfully",
            "data": article
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Article doesn't exist"
    }


@router.post("", response_description="Article added into the database", response_model=Response)
async def add_article_data(article: Article = Body(...)):
    new_article = await add_article(article)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Articles created successfully",
        "data": new_article
    }


@router.delete("/{id}", response_description="Article deleted successfully", response_model=Response)
async def delete_article_data(id: PydanticObjectId):
    deleted_article = await delete_article(id)
    if deleted_article:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Article with ID {} deleted".format(id),
            "data": deleted_article
        }
    return {
        "status_code": "404",
        "response_type": "error",
        "description": "Article with ID {} not found".format(id)
    }


@router.put("/{id}", response_description="Article data updated successfully", response_model=Response)
async def update_article(id: PydanticObjectId, req: UpdateArticleModel = Body(...)):
    updated_article = await update_article_data(id, req.dict())
    if updated_article:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Article with ID {} updated successfully".format(id),
            "data": update_article
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Article with ID {} not found".format(id)
    }
