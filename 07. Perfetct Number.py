def perfect_num(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."

number = int(input())

print(perfect_num(number))