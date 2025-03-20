cimport argparse
from app.crud.teachers import (
    create_teacher,
    read_teachers,
    update_teacher,
    delete_teacher,
)
from app.crud.groups import (
    create_group,
    read_groups,
    update_group,
    delete_group,
)
from app.crud.students import (
    create_student,
    read_students,
    update_student,
    delete_student,
)
from app.crud.subjects import (
    create_subject,
    read_subjects,
    update_subject,
    delete_subject,
)
from app.crud.grades import (
    create_grade,
    read_grades,
    update_grade,
    delete_grade,
)


def modify_database():
    print("Welcome to the Database Modification Interface")

    action = input("Enter action (create, read, update, delete): ").strip().lower()
    if action not in ["create", "read", "update", "delete"]:
        print(f"Invalid action '{action}'")
        return

    model = (
        input("Enter model (Teacher, Group, Student, Subject, Grade): ")
        .strip()
        .capitalize()
    )
    if model not in ["Teacher", "Group", "Student", "Subject", "Grade"]:
        print(f"Invalid model '{model}'")
        return

    args = {}
    if action in ["create", "update"]:
        if model == "Teacher":
            args["name"] = input("Enter name: ").strip()
        elif model == "Group":
            args["name"] = input("Enter name: ").strip()
        elif model == "Student":
            values = (
                input("Enter name and group ID (comma separated): ").strip().split(",")
            )
            args["name"] = values[0].strip()
            args["group_id"] = int(values[1].strip())
        elif model == "Subject":
            values = (
                input("Enter name and teacher ID (comma separated): ")
                .strip()
                .split(",")
            )
            args["name"] = values[0].strip()
            args["teacher_id"] = int(values[1].strip())
        elif model == "Grade":
            values = (
                input(
                    "Enter student ID, subject ID, grade, and date received (comma separated): "
                )
                .strip()
                .split(",")
            )
            args["student_id"] = int(values[0].strip())
            args["subject_id"] = int(values[1].strip())
            args["grade"] = int(values[2].strip())
            args["date_received"] = values[3].strip()
    if action in ["update", "delete"]:
        args["id"] = int(input("Enter ID: ").strip())

    model_actions = {
        "Teacher": {
            "create": lambda: create_teacher(args["name"]),
            "read": lambda: read_teachers(),
            "update": lambda: update_teacher(args["id"], args["name"]),
            "delete": lambda: delete_teacher(args["id"]),
        },
        "Group": {
            "create": lambda: create_group(args["name"]),
            "read": lambda: read_groups(),
            "update": lambda: update_group(args["id"], args["name"]),
            "delete": lambda: delete_group(args["id"]),
        },
        "Student": {
            "create": lambda: create_student(args["name"], args["group_id"]),
            "read": lambda: read_students(),
            "update": lambda: update_student(
                args["id"], args["name"], args["group_id"]
            ),
            "delete": lambda: delete_student(args["id"]),
        },
        "Subject": {
            "create": lambda: create_subject(args["name"], args["teacher_id"]),
            "read": lambda: read_subjects(),
            "update": lambda: update_subject(
                args["id"], args["name"], args["teacher_id"]
            ),
            "delete": lambda: delete_subject(args["id"]),
        },
        "Grade": {
            "create": lambda: create_grade(
                args["student_id"],
                args["subject_id"],
                args["grade"],
                args["date_received"],
            ),
            "read": lambda: read_grades(),
            "update": lambda: update_grade(
                args["id"],
                args["student_id"],
                args["subject_id"],
                args["grade"],
                args["date_received"],
            ),
            "delete": lambda: delete_grade(args["id"]),
        },
    }

    try:
        action_func = model_actions[model][action]
        action_func()
    except KeyError:
        print(f"Invalid action '{action}' for model '{model}'")
    except TypeError as e:
        print(
            f"Missing required arguments for action '{action}' on model '{model}': {e}"
        )
