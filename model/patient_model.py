from pydantic import BaseModel


class PatientCreate(BaseModel):
    id: int = 0
    first_name: str
    last_name:str 
    email: str
    phone_number: str
    address: str
    doctor_id: int
    status: bool = True

class PatientUpdate(BaseModel):
    first_name: str
    last_name:str 
    email: str
    phone_number: str
    address: str
    doctor_id: int
    status: bool = True