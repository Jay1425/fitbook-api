from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()

IST = ZoneInfo("Asia/Kolkata")


# ======================
# Book a Class
# ======================

@router.post("/book", response_model=schemas.BookingResponse)
def book_class(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    fitness_class = db.query(models.FitnessClass).filter(
        models.FitnessClass.id == booking.class_id
    ).first()

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    # Prevent overbooking
    if fitness_class.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Prevent duplicate booking by same user
    existing_booking = db.query(models.Booking).filter(
        models.Booking.class_id == booking.class_id,
        models.Booking.user_id == current_user.id
    ).first()

    if existing_booking:
        raise HTTPException(status_code=400, detail="You already booked this class")

    # Deduct slot
    fitness_class.availableSlots -= 1

    new_booking = models.Booking(
        class_id=booking.class_id,
        user_id=current_user.id,
        client_name=booking.client_name,
        client_email=booking.client_email,
        booked_at=datetime.now(IST)
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


# ======================
# Get User Bookings
# ======================

@router.get("/bookings", response_model=list[schemas.BookingResponse])
def get_user_bookings(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Booking).filter(
        models.Booking.user_id == current_user.id
    ).all()