rooms = int(input())
free_chairs = 0
is_game_on = True
for room in range(1, rooms + 1):
    chairs = input().split(' ')
    all_chairs = chairs[0]
    taken_chairs = int(chairs[1])
    if len(all_chairs) >= taken_chairs:
        diff = len(all_chairs) - taken_chairs
        free_chairs += diff
    else:
        is_game_on = False
        diff = taken_chairs - len(all_chairs)
        print(f'{diff} more chairs needed in room {room}')

if is_game_on:
    print(f'Game On, {free_chairs} free chairs left')
