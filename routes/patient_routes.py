from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from model.database_model import Patient
from database.database import get_db, templates

routes = APIRouter()

@routes.get("", response_description="Get all the patient details")
async def get_all_patient(request: Request, skip: int = 0, limit: int = 10, 
                          db: Session = Depends(get_db)):
    """
        This API will return all the patient details
    """ 
    try:
        get_patient = db.query(Patient).offset(skip).limit(limit).all()
        get_count_patient = db.query(Patient).count()
        return {"message": "Success", "data": get_patient, "count": get_count_patient}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Please try again {e}!")
