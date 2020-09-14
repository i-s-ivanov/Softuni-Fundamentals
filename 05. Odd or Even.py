cmd = input()
numbers = list(map(int, input().split()))

if cmd == 'Odd':
    filtered = sum(filter(lambda x: x % 2 == 1, numbers)) * len(numbers)
else:
    filtered = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)

print(filtered)

