from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from zoneinfo import ZoneInfo

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()

IST = ZoneInfo("Asia/Kolkata")


# ======================
# Create Fitness Class
# ======================

@router.post("/classes", response_model=schemas.ClassResponse)
def create_class(
    fitness_class: schemas.ClassCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Convert to IST timezone
    class_time = fitness_class.dateTime.astimezone(IST)

    new_class = models.FitnessClass(
        name=fitness_class.name,
        dateTime=class_time,
        instructor=fitness_class.instructor,
        availableSlots=fitness_class.availableSlots
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class


# ======================
# Get All Classes
# ======================

@router.get("/classes", response_model=list[schemas.ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    return db.query(models.FitnessClass).all()