def is_valid_index(length, index):
    return 0 <= idx < len(war_ship)


pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
length_warship = len(war_ship)
length_pirateship = len(pirate_ship)
max_health = int(input())

command_input = input()

while command_input != 'Retire':
    tokens = command_input.split()
    command = tokens[0]

    if command == 'Fire':
        idx = int(tokens[1])
        damage = int(tokens[2])

        if not is_valid_index(length_warship, idx):
            command_input = input()
            continue
        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            print(f'You won! The enemy ship has sunken.')
            break
    elif command == 'Defend':
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        damage = int(tokens[3])

        if not (is_valid_index(length_pirateship, first_index) and is_valid_index(length_pirateship, second_index)):
            command_input = input()
            continue

        for i in range(first_index, second_index + 1):
            pirate_ship[i] -= damage

            if pirate_ship[i] <= 0:
                print(f'You lost! The pirate ship has sunken.')
                break
    elif command == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])

        if not is_valid_index(length_pirateship, index):
            command_input = input()
            continue

        pirate_ship[index] += health

        if pirate_ship[index]
    elif command == 'Status':
        pass

    command_input = input()