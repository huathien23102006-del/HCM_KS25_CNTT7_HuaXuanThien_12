from pydantic import BaseModel, Field

class Create_appointment(BaseModel):
    patient_name: str=Field(...,min_length=2)
    doctor_name: str=Field(...,min_length=2)
    appointment_date: str=Field(...)
    status: str=Field(...)

