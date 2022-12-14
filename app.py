from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.article import router as ArticleRouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the WZ RestAPI POC"}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(ArticleRouter, tags=["Articles"], prefix="/article", dependencies=[Depends(token_listener)])
