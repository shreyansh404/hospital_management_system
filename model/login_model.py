from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"

class LoginModel(BaseModel):
    email: str
    password: str
    role: RoleEnum