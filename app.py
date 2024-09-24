from fastapi import FastAPI, Request
from routes.doctor_routes import routes as doctor_routes
from routes.authtentication import routes as auth_routes
from database.database import templates
from routes.patient_routes import routes as patient


app = FastAPI()

app.include_router(doctor_routes,tags=["Doctor"], prefix="/doctor")
app.include_router(auth_routes, tags=["Auth"], prefix="/auth")
app.include_router(patient, tags=["Patient"], prefix="/patient")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("hospital_management_system.html", {"request": request})

@app.get("/templates/{page}")
async def get_template(page:str,request: Request):
    print()
    return templates.TemplateResponse(f"{page}", {"request": request})
