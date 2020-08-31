numbers = input().split()
text = input()
result = []

for i in range(len(numbers)):
    total = 0
    for x in numbers[i]:
        total += int(x)
    length = len(text)
    if total >= length:
        index = total - length
    else:
        index = total
    result.append(text[index])
    text = text.replace(text[index], '', 1)

print(''.join(result))



