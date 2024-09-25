from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class VitalType(str, Enum):
    BODYTEMPERATURE = "body temperature"
    BP = "blood pressure"
    HEARTRATE = "heart rate"

class ReportCreation(BaseModel):
    id: int
    bp: str = 0
    bodytemp: int = 0
    heartrate: int = 0
    patient_id:int 
    created_at: int = int(datetime.now().timestamp())
