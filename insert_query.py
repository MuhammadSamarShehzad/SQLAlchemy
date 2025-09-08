from sqlalchemy import select
from connect import engine
from sqlalchemy.orm import Session
from models import Student, Courses, Enrollment

student_names = ["Ali Raza", "Sara Khan", "Umar Farooq", "Hina Malik", "Bilal Ahmed", "Ayesha Siddiqui", "Saif Ullah", "Nida Yasir"]

courses = [
    ("Computer Science", 50000),
    ("Data Science", 60000),
    ("Islamic Studies", 20000),
    ("Business Admin", 55000),
    ("Artificial Intelligence", 70000),
    ("Psychology", 40000),
    ("Software Engineering", 65000)
]

enrollment_data = [
    (1, 1, "2023-01-15"),
    (2, 2, "2023-02-20"),
    (3, 3, "2023-03-10"),
    (4, 4, "2023-04-05"),
    (5, 5, "2023-05-12"),
    (6, 6, "2023-06-18"),
    (7, 7, "2023-07-22"),
    (8, 1, "2023-08-30"),
    (3, 5, "2023-09-14"),
    (1, 2, "2023-10-03"),
    (2, 5, "2023-11-11"),
    (3, 1, "2023-12-25"),
    (4, 7, "2023-12-31")
]

with Session(engine) as session:

    # students = [Student(name=name) for name in student_names]
    # session.add_all(students)
    # session.commit()

    # courses = [Courses(name=name, fee=fee) for name, fee in courses]
    # session.add_all(courses)
    # session.commit()

    enrollments = [Enrollment(s_id=s_id, c_id=c_id, date=date) for s_id, c_id, date in enrollment_data]
    session.add_all(enrollments)
    session.commit()