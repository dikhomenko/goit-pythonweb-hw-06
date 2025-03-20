from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.database import engine
from db.models import teachers, subjects

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def create_teacher(name):
    teacher = teachers.insert().values(name=name)
    session.execute(teacher)
    session.commit()
    print(f"Teacher '{name}' created successfully.")


def read_teachers():
    result = session.execute(select([teachers]))
    for row in result:
        print(row)


def update_teacher(teacher_id, name):
    session.execute(
        teachers.update().where(teachers.c.id == teacher_id).values(name=name)
    )
    session.commit()
    print(f"Teacher with id={teacher_id} updated successfully.")


def delete_teacher(teacher_id):
    session.execute(
        subjects.delete().where(subjects.c.teacher_id == teacher_id)
    )  # Delete dependent subjects
    session.execute(teachers.delete().where(teachers.c.id == teacher_id))
    session.commit()
    print(f"Teacher with id={teacher_id} deleted successfully.")
