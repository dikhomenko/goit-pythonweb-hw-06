from app.queries.my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def run_queries():
    print("Top 5 students with the highest average grade:")
    print(select_1())

    subject_id = 31  # English
    print(f"Student with the highest average grade in subject {subject_id}:")
    print(select_2(subject_id))

    print(f"Average grade in groups for subject {subject_id}:")
    print(select_3(subject_id))

    print("Average grade across all grades:")
    print(select_4())

    teacher_id = 32  # Javier Atkins
    print(f"Courses taught by teacher {teacher_id}:")
    print(select_5(teacher_id))

    group_id = 33  # Group Lizzard
    print(f"List of students in group {group_id}:")
    print(select_6(group_id))

    print(f"Grades of students in group {group_id} for subject {subject_id}:")
    print(select_7(group_id, subject_id))

    print(f"Average grade given by teacher {teacher_id}:")
    print(select_8(teacher_id))

    student_id = 202  # Eric Gamble
    print(f"Courses attended by student {student_id}:")
    print(select_9(student_id))

    print(f"Courses taught by teacher {teacher_id} to student {student_id}:")
    print(select_10(student_id, teacher_id))
