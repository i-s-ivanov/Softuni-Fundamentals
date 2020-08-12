command_input = input()
judge = {}
total_points = {}

while command_input != 'no more time':
    tokens = command_input.split(' -> ')
    username = tokens[0]
    contest = tokens[1]
    points = int(tokens[2])
    if contest not in judge:
        judge[contest] = {}
    if username not in total_points:
        total_points[username] = 0
    total_points[username] += points
    if username in judge[contest]:
        total_points[username] = points
    if username not in judge[contest]:
        judge[contest][username] = 0
    if judge[contest][username] < points:
        judge[contest][username] = points
    command_input = input()


for k, v in judge.items():
    print(f'{k}: {len(v)} participants')
    sorted_v = dict(sorted(v.items(), key=lambda x: -x[1]))
    position = 1
    for q, w in sorted_v.items():
        print(f'{position}. {q} <::> {w}')
        position += 1
sorted_total_points = dict(sorted(total_points.items(), key=lambda o: (-o[1], o[0])))
print("Individual standings:")
pos = 1
for name, points in sorted_total_points.items():
    print(f'{pos}. {name} -> {points}')
    pos += 1