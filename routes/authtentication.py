from fastapi import APIRouter, Request, HTTPException, Depends, status
from sqlalchemy.orm import Session
from model.login_model import LoginModel, RoleEnum
from database.database import templates, get_db
from model.database_model import Doctor, Patient, Report
from database.helper_function import get_greeting
from sqlalchemy import func


routes = APIRouter()


@routes.post("/login", response_description="Login module")
async def login(payload: LoginModel, request: Request, db: Session = Depends(get_db)):
    """
        This API is used for login either doctor or patient
    """ 
    try:
        email_id = payload.email
        password = payload.password
        if payload.role == RoleEnum.DOCTOR:
        # Fetch doctor based on email and password in one query
            doctor_exists = db.query(Doctor).filter_by(email=email_id).first()        
            if doctor_exists:
                patients = db.query(Patient).all()
                get_count_patient = db.query(Patient).count()
                get_active_patient = db.query(Patient).filter(Patient.status == True).count()
                get_total_hr_added = db.query(Report).filter(Report.type == "heart rate").count()
                get_total_temperature_added = db.query(Report).filter(Report.type == "body temperature").count()  
                get_total_blood_pressure_added = db.query(Report).filter(Report.type == "blood pressure").count()  
                name = get_greeting() + " Dr " + doctor_exists.first_name + " " + doctor_exists.last_name
                return templates.TemplateResponse("doctor_dashboard.html", {
                    "request": request,
                    "get_active_patient": get_active_patient,
                    "doctor_name": name,
                    "get_total_hr_added":get_total_hr_added,
                    "get_total_temperature_added": get_total_temperature_added,
                    "get_total_blood_pressure_added": get_total_blood_pressure_added,
                    "doctor_email": doctor_exists.email,
                    "get_count_patient": get_count_patient,
                    "patients": patients,
                    "message": "Welcome Doctor!"
                })
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
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Please try again {e}!")
