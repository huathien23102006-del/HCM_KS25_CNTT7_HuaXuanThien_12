from fastapi import HTTPException, status
from model import AppointmentsModel
from sqlalchemy.orm import Session
from schemas import Create_appointment


def get_appointments(db: Session):
    return db.query(AppointmentsModel).all()

def get_appointment_status(status_appoint:str,db:Session):
    find_status = db.query(AppointmentsModel).filter(AppointmentsModel.status == status_appoint).first()
    if not find_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return find_status

def get_appoint_id(id: int, db:Session):
    find_id = db.query(AppointmentsModel).filter(AppointmentsModel.id == id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="NOT FOUND")
    return find_id

def create_appoint(input_appoint: Create_appointment, db: Session):
    new_appoint = AppointmentsModel(
        patient_name = input_appoint.patient_name,
        doctor_name = input_appoint.doctor_name,
        appointment_date = input_appoint.appointment_date,
        status = input_appoint.status
    )

    db.add(new_appoint)
    db.commit()
    db.refresh(new_appoint)

    return new_appoint

def update_appoint(id:int, input_appoint: Create_appointment, db: Session):
    find_id = db.query(AppointmentsModel).filter(AppointmentsModel.id == id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    find_id.patient_name = input_appoint.patient_name
    find_id.doctor_name = input_appoint.doctor_name
    find_id.appointment_date = input_appoint.appointment_date
    find_id.status = input_appoint.status

    db.commit()
    return find_id

def delete_appoint(id: int, db:Session):
    find_id = db.query(AppointmentsModel).filter(AppointmentsModel.id == id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    db.delete(find_id)
    db.commit()
    return {"status_code": 200}