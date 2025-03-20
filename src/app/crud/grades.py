from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.database import engine
from db.models import grades
from typing import List, Tuple

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def create_grade(
    student_id: int, subject_id: int, grade: int, date_received: str
) -> None:
    grade_entry = grades.insert().values(
        student_id=student_id,
        subject_id=subject_id,
        grade=grade,
        date_received=date_received,
    )
    session.execute(grade_entry)
    session.commit()
    print(
        f"Grade for student_id={student_id} and subject_id={subject_id} created successfully."
    )


def read_grades() -> List[Tuple]:
    result = session.execute(select([grades]))
    return result.fetchall()


def update_grade(
    grade_id: int, student_id: int, subject_id: int, grade: int, date_received: str
) -> None:
    session.execute(
        grades.update()
        .where(grades.c.id == grade_id)
        .values(
            student_id=student_id,
            subject_id=subject_id,
            grade=grade,
            date_received=date_received,
        )
    )
    session.commit()
    print(f"Grade with id={grade_id} updated successfully.")


def delete_grade(grade_id: int) -> None:
    session.execute(grades.delete().where(grades.c.id == grade_id))
    session.commit()
    print(f"Grade with id={grade_id} deleted successfully.")
