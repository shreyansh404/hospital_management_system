from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from model.login_model import LoginModel, RoleEnum
from database.database import templates, get_db
from model.model import Doctor, Patient
routes = APIRouter()

@routes.post("/login", response_description="Login")
async def login(payload: LoginModel, request: Request, db: Session = Depends(get_db)):
    """
    This API is used for login either doctor or patient
    """
    email_id = payload.email
    password = payload.password

    if payload.role == RoleEnum.DOCTOR:
        # Fetch doctor based on email and password in one query
        doctor_exists = db.query(Doctor).filter_by(email=email_id, password_hash=password).first()
        if doctor_exists:
            return templates.TemplateResponse("doctor_dashboard.html", {"request": request, "message": "Welcome Doctor!"})
        else:
            return templates.TemplateResponse("401.html",{"request": request,"message":"Invalid credentials for Doctor."})
    
    elif payload.role == RoleEnum.PATIENT:
        paitent_exits = db.query(Patient).filter_by(email=email_id, phone_number=password).first()
        if paitent_exits:
            patient_data = {
                "first_name": paitent_exits.first_name,
                "last_name": paitent_exits.last_name,
                "email": paitent_exits.email,
                "phone_number": paitent_exits.phone_number,
                "address": paitent_exits.address
            }
            print(patient_data)
            return templates.TemplateResponse("patient_detail.html", {"request": request, "patient": patient_data})
        else:
            return templates.TemplateResponse("401.html",{"request": request,"message":"Invalid credentials for Doctor."})

    
    else:
        return templates.TemplateResponse("404.html", {"request": request, "message": "Invalid role!."})
