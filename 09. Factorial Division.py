def factorial(a, b):
    first_factorial = 1
    second_factorial = 1
    for num in range(1, first_num + 1):
        first_factorial *= num
    for num in range(1, second_num + 1):
        second_factorial *= num
    return f'{first_factorial / second_factorial :.2f}'


first_num = int(input())
second_num = int(input())

print(factorial(first_num, second_num))
