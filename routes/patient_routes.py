from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from model.database_model import Patient
from model.patient_model import PatientUpdate
from database.database import get_db, templates

routes = APIRouter()


@routes.get("", response_description="Get all the patient details")
async def get_all_patient(
    request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    """
    This API will return all the patient details
    """
    try:
        get_patient = db.query(Patient).offset(skip).limit(limit).all()
        get_count_patient = db.query(Patient).count()
        return {"message": "Success", "data": get_patient, "count": get_count_patient}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Please try again {e}!",
        )


@routes.patch("/{patient_id}", response_description="Update the patient")
async def update_patient_helper(
    patient_id: int,
    request: Request,
    patientPayload: PatientUpdate,
    db: Session = Depends(get_db),
):
    """
    This function will update a patient by their ID.
    """
    try:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()

        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")

        if patientPayload.first_name:
            patient.first_name = patientPayload.first_name
        if patientPayload.last_name:
            patient.last_name = patientPayload.last_name
        if patientPayload.email:
            patient.email = patientPayload.email
        if patientPayload.phone_number:
            patient.phone_number = patientPayload.phone_number
        if patientPayload.address:
            patient.address = patientPayload.address
       
        patient.status = patientPayload.status
        db.commit()

        db.refresh(patient)

        return {"message": "Patient updated successfully", "patient": patient}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
