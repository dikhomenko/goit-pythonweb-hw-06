from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random
from datetime import datetime
from ..db.models import students, groups, teachers, subjects, grades
from ..db.database import engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

try:
    # Clear existing data
    session.execute(grades.delete())
    session.execute(students.delete())
    session.execute(subjects.delete())
    session.execute(teachers.delete())
    session.execute(groups.delete())
    session.commit()

    # Create groups
    group_names = ["Group Frog", "Group Toad", "Group Lizzard"]
    group_ids = []
    for name in group_names:
        group = groups.insert().values(name=name)
        result = session.execute(group)
        group_ids.append(result.inserted_primary_key[0])

    # Create teachers
    teacher_names = ["Joshua Lawrence", "Javier Atkins", "Mrs. Victoria Bennett"]
    teacher_ids = []
    for name in teacher_names:
        teacher = teachers.insert().values(name=name)
        result = session.execute(teacher)
        teacher_ids.append(result.inserted_primary_key[0])

    # Create subjects
    subject_names = ["English", "Physics", "Biology", "Basketball", "History"]
    subject_ids = []
    for i, name in enumerate(subject_names):
        teacher_id = teacher_ids[i % len(teacher_ids)]  # Round-robin assignment
        subject = subjects.insert().values(name=name, teacher_id=teacher_id)
        result = session.execute(subject)
        subject_ids.append(result.inserted_primary_key[0])

    # Create students
    student_names = [fake.name() for _ in range(30)]
    student_ids = []
    for name in student_names:
        group_id = random.choice(group_ids)
        student = students.insert().values(name=name, group_id=group_id)
        result = session.execute(student)
        student_ids.append(result.inserted_primary_key[0])

    # Create grades
    for _ in range(100):
        grade = grades.insert().values(
            student_id=random.choice(student_ids),
            subject_id=random.choice(subject_ids),
            grade=random.randint(1, 100),
            date_received=fake.date(),
        )
        session.execute(grade)

    # Commit the session
    session.commit()

    print("Database seeded successfully.")

except Exception as e:
    # Rollback the session in case of error
    session.rollback()
    print(f"An error occurred: {e}")

finally:
    # Close the session
    session.close()
