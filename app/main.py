from fastapi import FastAPI
from app.database import Base, engine
from app import models

app = FastAPI(title="FitBook API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FitBook API is running 🚀"}