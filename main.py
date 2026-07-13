from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import appointment_service
from schemas import Create_appointment 
app = FastAPI(
    title="Quản Lí Lịch Hẹn Phòng Khám"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def test_server():
    return{"message":"API đang chạy"}

@app.get("/appointments")
def get_appointments(db: Session=Depends(get_db)):
    return appointment_service.get_appointments(db)

@app.get("/appointments/search?status=...")
def get_appoint_by_status(status: str, db: Session=Depends(get_db)):
    return appointment_service.get_appointment_status(status, db)

@app.get("/appointments/{appointment_id}")
def get_appointment_id(id: int, db:Session=Depends(get_db)):
    return appointment_service.get_appoint_id(id, db)

@app.post("/appointments")
def create_appoint(input_appoint: Create_appointment, db: Session=Depends(get_db)):
    return appointment_service.create_appoint(input_appoint,db)

@app.put("/appointments/{appointment_id}")
def update_appoint(id: int, input_appoint: Create_appointment, db: Session=Depends(get_db)):
    return appointment_service.update_appoint(id, input_appoint, db)

@app.delete("/appointments/{appointment_id}")
def delete_appoint(id: int, db: Session=Depends(get_db)):
    return appointment_service.delete_appoint(id, db)