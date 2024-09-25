from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database.database import get_db 
from model.docter_model import DoctorCreate
from model.model import Doctor, Patient
from database.database import templates
from database.helper_function import generate_unique_id
routes = APIRouter()

@routes.get("/dashboard", response_description="Dashboard Detail")
async def get_dashboard_details(doctor_id: int, db: Session = Depends(get_db)):
    patient_count = db.query(Patient).filter_by(doctor_id=doctor_id).count()
    return {"patients": patient_count}


@routes.post("/patient", response_description="Add Doctor")
async def register_patient(request: Request, doctor: DoctorCreate, db:Session = Depends(get_db)):
    try:
        doctor.id = generate_unique_id()
        new_doctor= Doctor(**doctor.dict())
        db.add(new_doctor)
        db.commit()
        return templates.TemplateResponse("doctor_dashboard.html", {"request": request})
    except Exception as e:
        return {"Error": f"Please try again {e}"}
@routes.patch("/patient/{patient_id}", response_description="Update patient")
async def update_patient(patient_id: int, patient: DoctorCreate, db: Session = Depends(get_db)):
    db.query(Patient).filter(Patient.id == patient_id).update(patient.dict())
    db.commit()
    return {"message": "Patient updated successfully"}


