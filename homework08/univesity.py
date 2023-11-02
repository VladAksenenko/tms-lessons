from student import Student

students = [Student('Ivan', 9),
            Student('Vlad', 6),
            Student('Denis', 4),
            Student('Dima', 10)]


def calc_sum_scholarship(lst: list) -> int:
    sum_scholarship = 0
    for student in lst:
        sum_scholarship += student.get_scholarship()
    return sum_scholarship


def get_excellent_student_count(lst: list) -> int:
    count = 0
    for student in lst:
        if student.is_excellent():
            count += 1
    return count


print(calc_sum_scholarship(students))
print(get_excellent_student_count(students))