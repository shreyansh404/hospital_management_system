from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base

# Patient model
class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    address = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    status = Column(Boolean, default=True)
    
# Doctor model
class Doctor(Base):
    __tablename__ = "doctor"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    

# Report model
class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, )
    value = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    patient_id = Column(Integer)