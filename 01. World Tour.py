string = input()
cmd_input = input()

while cmd_input != 'Travel':
    tokens = cmd_input.split(':')
    cmd = tokens[0]
    if cmd == 'Add Stop':
        index = int(tokens[1])
        sub = tokens[2]
        if 0 <= index < len(string):
            l = list(string)
            l.insert(index, sub)
            string = ''.join(l)
        print(string)
    elif cmd == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index <= end_index < len(string):
            substring = string[start_index:end_index + 1]
            string = string.replace(substring, '', 1)
        print(string)
    elif cmd == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
        print(string)

    cmd_input = input()

print(f'Ready for world tour! Planned stops: {string}')