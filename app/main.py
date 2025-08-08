from fastapi import FastAPI

app = FastAPI()

from app.routes.routes import routes

app.include_router(routes)