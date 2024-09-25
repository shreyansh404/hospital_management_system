from pydantic import BaseModel


class PatientCreate(BaseModel):
    id: int
    first_sname: str
    last_name:str 
    email: str
    phone_number: str
    address: str
    doctor_id: int
    status: bool = True