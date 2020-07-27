divisor = int(input())
bound = int(input())

for num in range(1, bound + 1):
    if num % divisor == 0:
        found = num

print(found)
