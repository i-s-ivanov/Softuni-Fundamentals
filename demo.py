n = int(input())
guests = []
arrived_guests = []

for _ in range(n):
    guest = input()
    guests.append(guest)

cmd = input()
while cmd != "END":
    arrived_guests.append(cmd)
    cmd = input()

did_not_come = set(guests) - set(arrived_guests)
did_not_come = sorted(did_not_come)
print(len(did_not_come))
[print(x) for x in did_not_come if x[0].isdigit()]
[print(x) for x in did_not_come if x[0].isalpha()]