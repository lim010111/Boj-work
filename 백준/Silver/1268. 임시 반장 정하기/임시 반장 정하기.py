def solution():
    student_info = {i:set() for i in range(1, n + 1)} # counts of students whom has met ith student.
    
    for c in range(5):
        prev_class_info = {i:set() for i in range(1, 9 + 1)}
        for r in range(n):
            prev_class_info[matrix[r][c]].add(r+1)

        for prev_class in prev_class_info:
            if len(prev_class_info[prev_class]) > 1:
                for student in prev_class_info[prev_class]:
                    student_info[student].update(prev_class_info[prev_class])

    for student in student_info:
        if len(student_info[student]):
            student_info[student] = student_info[student] - {student}
    return max(student_info, key=lambda x: (len(student_info[x]), -x))


if __name__ == "__main__":
    n = int(input()) # Numbers of students
    matrix = [list(map(int, input().split())) for _ in range(n)] # row: class of nth student in 5 years
    print(solution())