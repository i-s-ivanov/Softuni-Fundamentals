n = int(input())
students = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

average_grades = {}

for k, v in students.items():
    average_grade = sum(v) / len(v)
    if average_grade < 4.5:
        continue
    average_grades[k] = average_grade

average_grades = dict(sorted(average_grades.items(), key=lambda x: x[1], reverse=True))

for k, v in average_grades.items():
    print(f'{k} -> {v:.2f}')