ops = ('multiply', 'divide', 'add', 'subtract')

op = input()
a = int(input())
b = int(input())


def calc(a, b, op):
    if op == ops[0]:
        return a * b
    elif op == ops[1]:
        return int(a / b)
    elif op == ops[2]:
        return a + b
    elif op == ops[3]:
        return a - b


print(calc(a, b, op))
