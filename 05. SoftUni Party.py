n = int(input())
guest = []
arrived_guests = []

for _ in range(n):
    name = input()
    guest.append(name)

name = input()
while name != 'END':
    arrived_guests.append(name)
    name = input()

did_not_come = set(guest) - set(arrived_guests)
did_not_come = sorted(did_not_come)
print(len(did_not_come))
[print(guest) for guest in did_not_come if guest[0].isdigit()]
[print(guest) for guest in did_not_come if guest[0].isalpha()]
