n = int(input())
numbers = []

for _ in range(n):
    tokens = input().split()
    cmd = tokens[0]
    if cmd == '1':
        num = int(tokens[1])
        numbers.append(num)
    elif cmd == '2':
        if numbers:
            numbers.pop()
    elif cmd == '3':
        if numbers:
            print(max(numbers))
    elif cmd == '4':
        if numbers:
            print(min(numbers))

print(', '.join([str(x) for x in reversed(numbers)]))