from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="FitBook API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FitBook API is running 🚀"}