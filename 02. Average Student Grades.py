count = int(input())
students = {}

for i in range(count):
    name_grade = input().split()
    name = name_grade[0]
    grade = float(name_grade[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)


for (key, values) in students.items():
    average = f'{sum(values) / len(values):.2f}'
    values = " ".join(f'{value:.2f}' for value in values)
    print(f"{key} -> {values} (avg: {average})")