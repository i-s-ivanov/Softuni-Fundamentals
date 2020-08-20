
def sum_of_even_and_odd(text):
    even_sum = 0
    odd_sum = 0
    for i in text:
        num = int(i)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


text = input()
print(sum_of_even_and_odd(text))
