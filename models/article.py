from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel


schema_example = {
    "example": {
        "title": "News aus dem Emmental",
        "subtitle": "Zäziwil",
        "detail": "Im Emmental nichts Neues",
        "author": 10,
        "summary": "Zusammenfassung vom Beitrag"
    }
}


class Article(Document):
    title: str
    subtitle: str
    detail: str
    author: int
    summary: str

    class Config:
        schema_extra = schema_example


class UpdateArticleModel(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    detail: Optional[str]
    author: Optional[int]
    summary: Optional[str]

    class Collection:
        name = "article"

    class Config:
        schema_extra = schema_example


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
