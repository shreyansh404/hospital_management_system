from sqlalchemy.orm import Session
from database.database import engine, Base, SessionLocal  
from model.database_model import Patient, Doctor, Report 
from datetime import datetime

def seed_data(db: Session):
    doctor_1 = Doctor(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        password_hash="hashedpassword1" 
    )
    
    doctor_2 = Doctor(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        password_hash="hashedpassword2"
    )

    db.add(doctor_1)
    db.add(doctor_2)

    patient_1 = Patient(
        first_name="Dashrath",
        last_name="Lal Soni",
        email="d.lalsoni@example.com",
        phone_number="1234567890",
        address="Pune",
        doctor_id=1,  
        status=True
    )
    
    patient_2 = Patient(
        first_name="Ramesh",
        last_name="Verma",
        email="ramesh.verma@example.com",
        phone_number="0987654321",
        address="Mumbai",
        doctor_id=2, 
        status=True
    )

    db.add(patient_1)
    db.add(patient_2)

    report_1 = Report(
        type="BP",
        value="120/80",
        patient_id=1
    )
    
    report_2 = Report(
        type="Heart Rate",
        value="75 BPM",
        patient_id=2
    )
    
    report_3 = Report(
        type="Body Temperature",
        value="98.6 F",
        patient_id=1
    )

    db.add(report_1)
    db.add(report_2)
    db.add(report_3)

    try:
        db.commit()
        print("Seed data successfully added!")
    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    seed_data(db)
