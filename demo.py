line = input()
contests = {}

while line != 'end of contests':
    language, password = line.split(':')
    if language not in contests:
        contests[language] = ''
    contests[language] = password
    line = input()

submissions = {}
sub = input()

while sub != 'end of submissions':
    tokens = sub.split('=>')
    contest = tokens[0]
    password_for_contest = tokens[1]
    username = tokens[2]
    points = int(tokens[3])
    if contest in contests and password_for_contest == contests[contest]:
        if username not in submissions:
            submissions[username] = {}
            if contest not in submissions[username]:
                submissions[username][contest] = points
        else:
            if contest not in submissions[username]:
                submissions[username][contest] = points
            else:
                if submissions[username][contest] < points:
                    submissions[username][contest] = points
    sub = input()


winner = ''
win = 0
for k, v in submissions.items():
    total = 0
    for t, c in v.items():
        total += c
    if total > win:
        win = total
        winner = k

print(f'Best candidate is {winner} with total {win} points.')
print('Ranking:')
sorted_submission = dict(sorted(submissions.items()))

for key, key1 in sorted_submission.items():
    print(key)
    sorted_key1 = dict(sorted(key1.items(), key=lambda o: -o[1]))
    for q, w in sorted_key1.items():
        print(f'#  {q} -> {w}')