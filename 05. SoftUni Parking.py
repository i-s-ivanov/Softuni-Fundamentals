n = int(input())
parking = {}

for _ in range(n):
    tokens = input().split()
    command = tokens[0]
    username = tokens[1]
    if command == 'register':
        license_plate = tokens[2]
        if username in parking:
            print(f'ERROR: already registered with plate number {license_plate}')
            continue
        parking[username] = license_plate
        print(f'{username} registered {license_plate} successfully')
    elif command == 'unregister':
        if username not in parking:
            print(f'ERROR: user {username} not found')
            continue
        parking.pop(username)
        print(f'{username} unregistered successfully')

for k, v in parking.items():
    print(f'{k} => {v}')
