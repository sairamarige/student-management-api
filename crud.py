from sqlalchemy.orm import Session
import models

def create_student(db: Session, student):
    obj = models.Student(**student.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def update_student(db: Session, student_id: int, student):

    obj = get_student(db, student_id)

    if obj is None:
        return None

    for key, value in student.model_dump().items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)

    return obj


def patch_student(db: Session, student_id: int, student):

    obj = get_student(db, student_id)

    if obj is None:
        return None

    update_data = student.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)

    return obj


def delete_student(db: Session, student_id: int):

    obj = get_student(db, student_id)

    if obj is None:
        return None

    db.delete(obj)
    db.commit()

    return obj