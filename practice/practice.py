def get_top_student(students) -> str:
    top_student = ("placeholder", 0)
    for student in students:
        if student[1] > top_student[1]:
            top_student = student
    return top_student[0]
        

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]

print(get_top_student(students))

print(str(max(students, key=lambda x: x[1])[0] if students else None))
