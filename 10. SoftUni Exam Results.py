line = input()
exams_result = {}
submissions = {}

while line != 'exam finished':
    tokens = line.split('-')
    name = tokens[0]
    language = tokens[1]
    if language == 'banned':
        exams_result.pop(name)
        line = input()
        continue
    result = int(tokens[2])
    if name not in exams_result:
        exams_result[name] = result
    else:
        if result > exams_result[name]:
            exams_result[name] = result
    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1
    line = input()

exams_result_sorted = dict(sorted(exams_result.items(), key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(submissions.items(), key=lambda k: (-k[1], k[0])))

print('Results:')
for k, v in exams_result_sorted.items():
    print(f'{k} | {v}')
print('Submissions:')
for key, value in sorted_submissions.items():
    print(f'{key} - {value}')