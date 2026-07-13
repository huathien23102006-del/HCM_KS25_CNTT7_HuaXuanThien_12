from sqlalchemy import Column, Integer, String
from database import Base
class AppointmentsModel(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String(100), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    appointment_date = Column(String(100), nullable=False)
    status = Column(String(255), nullable=False)