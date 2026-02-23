from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from zoneinfo import ZoneInfo

from app.database import Base


IST = ZoneInfo("Asia/Kolkata")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    bookings = relationship("Booking", back_populates="user", cascade="all, delete")


class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dateTime = Column(DateTime(timezone=True), nullable=False)
    instructor = Column(String, nullable=False)
    availableSlots = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="fitness_class", cascade="all, delete")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    class_id = Column(Integer, ForeignKey("fitness_classes.id"))
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    booked_at = Column(DateTime(timezone=True), default=lambda: datetime.now(IST))

    user = relationship("User", back_populates="bookings")
    fitness_class = relationship("FitnessClass", back_populates="bookings")