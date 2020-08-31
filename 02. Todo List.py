notes = []

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    priority = int(tokens[0])
    note = tokens[1]
    notes.append((priority, note))


def sort_fn(element):
    return element[0]


sorted_task = sorted(notes, key=sort_fn)
print([task[1] for task in sorted_task])
