import math

name = input()
played_games = int(input())
volleyball_counter = 0
tennis_counter = 0
badminton_counter = 0
volleyball_total = 0
tennis_total = 0
badminton_total = 0

for i in range(played_games):
    name_of_game = input()
    points = int(input())
    if name_of_game == 'volleyball':
        volleyball_total += points + points * 0.07
        volleyball_counter += 1
    elif name_of_game == 'tennis':
        tennis_total += points + points * 0.05
        tennis_counter += 1
    elif name_of_game == 'badminton':
        badminton_total += points + points * 0.02
        badminton_counter += 1

total = volleyball_total + tennis_total + badminton_total

if math.floor(volleyball_total / volleyball_counter) < 75 or math.floor(tennis_total / tennis_counter) < 75 or math.floor(badminton_total / badminton_counter) < 75:
    print(f'Sorry, {name}, you lost. Your points are only {math.floor(total)}.')
else:
    print(f'Congratulations, {name}! You won the cruise games with {math.floor(total)} points.')