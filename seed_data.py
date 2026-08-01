from database import engine, SessionLocal
from models import Base, Student

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Student).count() == 0:

    students = [
        Student(name="Rahul", age=22, email="rahul@gmail.com", course="Python"),
        Student(name="Priya", age=21, email="priya@gmail.com", course="Java"),
        Student(name="Kiran", age=23, email="kiran@gmail.com", course="AI"),
        Student(name="Sneha", age=22, email="sneha@gmail.com", course="ML"),
        Student(name="Arjun", age=24, email="arjun@gmail.com", course="Data Science"),
        Student(name="Ravi", age=22, email="ravi@gmail.com", course="SQL"),
        Student(name="Meena", age=21, email="meena@gmail.com", course="Power BI"),
        Student(name="Akash", age=23, email="akash@gmail.com", course="FastAPI"),
        Student(name="Divya", age=22, email="divya@gmail.com", course="React"),
        Student(name="Vikram", age=24, email="vikram@gmail.com", course="Cloud")
    ]

    db.add_all(students)
    db.commit()

db.close()

print("Database Seeded Successfully")