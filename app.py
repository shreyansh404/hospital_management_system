from fastapi import FastAPI, Request
from routes.doctor_routes import routes as doctor_routes
from routes.authtentication import routes as auth_routes
from database.database import templates
from routes.patient_routes import routes as patient
from fastapi.middleware.cors import CORSMiddleware
from routes.report_routes import routes as report


app = FastAPI()

origins = [
    "http::127.0.0.1:8943",
    "http://localhost:8943"   # Allow localhost too

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doctor_routes,tags=["Doctor"], prefix="/doctor")
app.include_router(auth_routes, tags=["Auth"], prefix="/auth")
app.include_router(patient, tags=["Patient"], prefix="/patient")
app.include_router(report, tags=["Report"], prefix="/report")

@app.get("/")
async def get_root(request: Request):
    print("Inside the home page.")
    return templates.TemplateResponse("hospital_management_system.html", {"request": request})

@app.get("/templates/{page}")
async def get_template(page:str,request: Request):
    return templates.TemplateResponse(f"{page}", {"request": request})

@app.get("/templates/add/patient", response_description="Added Paitent")
async def add_paitent_helper(request: Request):
    return templates.TemplateResponse("add_paitent.html", {"request": request})