from pydantic import BaseModel, EmailStr
from datetime import datetime


# ======================
# User Schemas
# ======================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {
    "from_attributes": True
    }


class Token(BaseModel):
    access_token: str
    token_type: str


# ======================
# Class Schemas
# ======================

class ClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int


class ClassResponse(BaseModel):
    id: int
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

    model_config = {
    "from_attributes": True
    }


# ======================
# Booking Schemas
# ======================

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr


class BookingResponse(BaseModel):
    id: int
    class_id: int
    user_id: int
    client_name: str
    client_email: EmailStr
    booked_at: datetime

    model_config = {
    "from_attributes": True
    }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

