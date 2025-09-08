from sqlalchemy import select, func
from connect import engine
from sqlalchemy.orm import Session
from models import User, Address, Student, Courses, Enrollment

# with Session(engine) as session:
#     stmlt = select(User)
#     users = session.scalars(stmlt).all()
#     for user in users:
#         print(user)


# with Session(engine) as session:
#     students = session.query(Enrollment).all()
#     for student in students:
#         print(student)

# with Session(engine) as session:
#     data = session.query(Student.name, Enrollment.date, Courses.name).join(Enrollment, Student.id == Enrollment.s_id).join(Courses, Courses.id == Enrollment.c_id).all()

#     for item in data:
#         print(item)


# with Session(engine) as session:
#     stmt = session.query(
#         Student.name,
#         func.count(Enrollment.c_id).label("total_courses")
#     ).join(Enrollment, Student.id == Enrollment.s_id)\
#      .group_by(Student.name)

#     results = stmt.all()
#     for name, total in results:
#         print(name, total)


with Session(engine) as session:
    data = session.query(Student.name, func.sum(Courses.fee).label("total_fee"))\
    .join(Enrollment, Student.id == Enrollment.s_id)\
    .join(Courses, Courses.id == Enrollment.c_id)\
    .group_by(Student.name)

    for data in data:
        print(data)
        