numbers = [int(x) for x in input().split()]
stack = []

while numbers:
    stack.append(numbers.pop())

print(' '.join([str(x) for x in stack]))