n = int(input())
capacity = 255
sum = 0

for i in range(n):
    water = int(input())
    if water > capacity:
        print('Insufficient capacity!')
        continue
    else:
        capacity -= water
        sum += water

print(sum)