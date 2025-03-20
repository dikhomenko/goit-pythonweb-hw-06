from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.database import engine
from db.models import students, grades
from typing import List, Tuple

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def create_student(name: str, group_id: int) -> None:
    student = students.insert().values(name=name, group_id=group_id)
    session.execute(student)
    session.commit()
    print(f"Student '{name}' created successfully.")


def read_students() -> List[Tuple]:
    result = session.execute(select([students]))
    return result.fetchall()


def update_student(student_id: int, name: str, group_id: int) -> None:
    session.execute(
        students.update()
        .where(students.c.id == student_id)
        .values(name=name, group_id=group_id)
    )
    session.commit()
    print(f"Student with id={student_id} updated successfully.")


def delete_student(student_id: int) -> None:
    session.execute(
        grades.delete().where(grades.c.student_id == student_id)
    )  # Delete dependent grades
    session.execute(students.delete().where(students.c.id == student_id))
    session.commit()
    print(f"Student with id={student_id} deleted successfully.")
