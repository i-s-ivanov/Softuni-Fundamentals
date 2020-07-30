letter_count = int(input())
sum = 0

for i in range(letter_count):
    letter = input()
    value = ord(letter)
    sum += value
print(f'The sum equals: {sum}')