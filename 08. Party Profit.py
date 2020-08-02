import math

party_size = int(input())
days = int(input())
sum = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    sum += 50
    sum -= party_size * 2
    if i % 3 == 0:
        sum -= party_size * 3
    if i % 5 == 0:
        sum += 20 * party_size
        if i % 3 == 0:
            sum -= party_size * 2

coins = math.floor(sum / party_size)
print(f'{party_size} companions received {coins} coins each.')