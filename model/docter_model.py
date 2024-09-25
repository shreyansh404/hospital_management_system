from pydantic import BaseModel

class DoctorCreate(BaseModel):
    id: int= 1
    first_name: str
    last_name: str
    email: str
    password_hash: str