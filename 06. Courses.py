text = input()

courses = {}
while text != 'end':
    args = text.split(' : ')
    courses_name = args[0]
    student_name = args[1]
    if courses_name not in courses:
        courses[courses_name] = []
    courses[courses_name].append(student_name)


    text = input()

sorted_courses = dict(sorted(courses.items(), key= lambda x: (len(x[1])), reverse=True))

for key, value in sorted_courses.items():
    print(f'{key}: {len(value)}')

    for student_name in sorted(value):
        print(f'-- {student_name}')