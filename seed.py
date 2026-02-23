# seed.py
from app.database import SessionLocal
from app.models import FitnessClass
from datetime import datetime
from zoneinfo import ZoneInfo

db = SessionLocal()

ist = ZoneInfo("Asia/Kolkata")

sample_class = FitnessClass(
    name="Demo Yoga",
    dateTime=datetime.now(ist),
    instructor="Demo Instructor",
    availableSlots=10
)

db.add(sample_class)
db.commit()
db.close()

print("Seed data inserted successfully.")