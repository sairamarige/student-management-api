from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student REST API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Student REST API"}


@app.post("/students", response_model=schemas.StudentResponse)
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


@app.get("/students", response_model=list[schemas.StudentResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def read_one(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return student


@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update(student_id: int,
           student: schemas.StudentCreate,
           db: Session = Depends(get_db)):

    updated = crud.update_student(db, student_id, student)

    if updated is None:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return updated


@app.patch("/students/{student_id}", response_model=schemas.StudentResponse)
def patch(student_id: int,
          student: schemas.StudentUpdate,
          db: Session = Depends(get_db)):

    updated = crud.patch_student(db, student_id, student)

    if updated is None:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return updated


@app.delete("/students/{student_id}")
def delete(student_id: int,
           db: Session = Depends(get_db)):

    deleted = crud.delete_student(db, student_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return {"message": "Student Deleted Successfully"}