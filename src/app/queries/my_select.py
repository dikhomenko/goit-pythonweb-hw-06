from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, desc
from db.models import students, groups, teachers, subjects, grades
from db.database import engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = (
        session.query(students.c.name, func.avg(grades.c.grade).label("average_grade"))
        .join(grades, students.c.id == grades.c.student_id)
        .group_by(students.c.id)
        .order_by(desc("average_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2(subject_id):
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = (
        session.query(students.c.name, func.avg(grades.c.grade).label("average_grade"))
        .join(grades, students.c.id == grades.c.student_id)
        .filter(grades.c.subject_id == subject_id)
        .group_by(students.c.id)
        .order_by(desc("average_grade"))
        .first()
    )
    return result


def select_3(subject_id):
    # Знайти середній бал у групах з певного предмета.
    result = (
        session.query(groups.c.name, func.avg(grades.c.grade).label("average_grade"))
        .join(students, groups.c.id == students.c.group_id)
        .join(grades, students.c.id == grades.c.student_id)
        .filter(grades.c.subject_id == subject_id)
        .group_by(groups.c.id)
        .all()
    )
    return result


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.avg(grades.c.grade).label("average_grade")).all()
    return result


def select_5(teacher_id):
    # Знайти які курси читає певний викладач.
    result = (
        session.query(subjects.c.name).filter(subjects.c.teacher_id == teacher_id).all()
    )
    return result


def select_6(group_id):
    # Знайти список студентів у певній групі.
    result = (
        session.query(students.c.name).filter(students.c.group_id == group_id).all()
    )
    return result


def select_7(group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    result = (
        session.query(students.c.name, grades.c.grade)
        .join(grades, students.c.id == grades.c.student_id)
        .filter(students.c.group_id == group_id)
        .filter(grades.c.subject_id == subject_id)
        .all()
    )
    return result


def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = (
        session.query(func.avg(grades.c.grade).label("average_grade"))
        .join(subjects, grades.c.subject_id == subjects.c.id)
        .filter(subjects.c.teacher_id == teacher_id)
        .all()
    )
    return result


def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    result = (
        session.query(subjects.c.name)
        .join(grades, subjects.c.id == grades.c.subject_id)
        .filter(grades.c.student_id == student_id)
        .all()
    )
    return result


def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    result = (
        session.query(subjects.c.name)
        .join(grades, subjects.c.id == grades.c.subject_id)
        .filter(grades.c.student_id == student_id)
        .filter(subjects.c.teacher_id == teacher_id)
        .all()
    )
    return result


# Close the session
session.close()
