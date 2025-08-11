from fastapi import FastAPI
from app.routes.routes import router
from app.database import database, models
app = FastAPI()

models.Base.metadata.create_all(bind=database.db)

app.include_router(router)