from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from model.docter_model import DoctorCreate
from model.patient_model import PatientCreate
from model.database_model import Doctor, Patient
from database.database import templates
from database.helper_function import generate_unique_id

routes = APIRouter()


@routes.get("/dashboard", response_description="Dashboard Detail")
async def get_dashboard_details(doctor_id: int, db: Session = Depends(get_db)):
    patient_count = db.query(Patient).filter_by(doctor_id=doctor_id).count()
    return {"patients": patient_count}


@routes.post("/patient", response_description="Add Doctor")
async def register_patient(
    request: Request, doctor: PatientCreate, db: Session = Depends(get_db)
):
    try:
        doctor.id = generate_unique_id()
        exist_patient = (
            db.query(Patient)
            .filter(
                Patient.email == doctor.email,
                Patient.phone_number == doctor.phone_number,
            )
            .first()
        )
        if exist_patient:
            return {"message": "Patient Already exists!"}
        new_doctor = Patient(**doctor.dict())
        db.add(new_doctor)
        db.commit()
        return templates.TemplateResponse("doctor_dashboard.html", {"request": request})

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Please try again {e}!",
        )


@routes.patch("/patient/{patient_id}", response_description="Update patient")
async def update_patient(
    patient_id: int, patient: DoctorCreate, db: Session = Depends(get_db)
):
    try:
        db.query(Patient).filter(Patient.id == patient_id).update(patient.dict())
        db.commit()
        return {"message": "Patient updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Please try again {e}!",
        )

@routes.get("/", response_description="Get all doctors")
async def get_all_doctor(request: Request, db: Session = Depends(get_db)):
    """
        This API will return all the doctor 
    """
    doctor = db.query(Doctor).all()
    return doctor