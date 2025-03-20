from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.database import engine
from db.models import groups, students
from typing import List, Tuple

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()


def create_group(name: str) -> None:
    group = groups.insert().values(name=name)
    session.execute(group)
    session.commit()
    print(f"Group '{name}' created successfully.")


def read_groups() -> List[Tuple]:
    result = session.execute(select([groups]))
    return result.fetchall()


def update_group(group_id: int, name: str) -> None:
    session.execute(groups.update().where(groups.c.id == group_id).values(name=name))
    session.commit()
    print(f"Group with id={group_id} updated successfully.")


def delete_group(group_id: int) -> None:
    session.execute(
        students.delete().where(students.c.group_id == group_id)
    )  # Delete dependent students
    session.execute(groups.delete().where(groups.c.id == group_id))
    session.commit()
    print(f"Group with id={group_id} deleted successfully.")
