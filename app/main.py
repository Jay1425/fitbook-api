from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import users

app = FastAPI(title="FitBook API")
app.include_router(users.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FitBook API is running 🚀"}


