numbers_list = [int(x) for x in input().split(", ")]
result = 1
n = len(numbers_list)
for number in numbers_list:
    if number <= 5:
        result *= number
    elif number > 5 and number <= 10:
        result /= number

print(result)
