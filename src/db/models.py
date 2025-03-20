from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column(
        "group_id",
        Integer,
        ForeignKey("groups.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)

groups = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

teachers = Table(
    "teachers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

subjects = Table(
    "subjects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column(
        "teacher_id",
        Integer,
        ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
)

grades = Table(
    "grades",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "student_id",
        Integer,
        ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "subject_id",
        Integer,
        ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column("grade", Integer, nullable=False),
    Column("date_received", String, nullable=False),
)
