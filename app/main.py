from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import users, classes, bookings


app = FastAPI(title="FitBook API")
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FitBook API is running 🚀"}


