from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.database import engine
from db.models import subjects, grades
from typing import List, Tuple

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def create_subject(name: str, teacher_id: int) -> None:
    subject = subjects.insert().values(name=name, teacher_id=teacher_id)
    session.execute(subject)
    session.commit()
    print(f"Subject '{name}' created successfully.")


def read_subjects() -> List[Tuple]:
    result = session.execute(select([subjects]))
    return result.fetchall()


def update_subject(subject_id: int, name: str, teacher_id: int) -> None:
    session.execute(
        subjects.update()
        .where(subjects.c.id == subject_id)
        .values(name=name, teacher_id=teacher_id)
    )
    session.commit()
    print(f"Subject with id={subject_id} updated successfully.")


def delete_subject(subject_id: int) -> None:
    session.execute(
        grades.delete().where(grades.c.subject_id == subject_id)
    )  # Delete dependent grades
    session.execute(subjects.delete().where(subjects.c.id == subject_id))
    session.commit()
    print(f"Subject with id={subject_id} deleted successfully.")
