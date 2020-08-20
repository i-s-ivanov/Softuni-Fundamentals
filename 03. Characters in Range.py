def chars_between_them(a, b):
    list = []
    start = ord(min([a, b]))
    end = ord(max([a, b]))
    for char in range(start + 1, end):
        list.append(chr(char))
    return list


char1 = input()
char2 = input()
result = chars_between_them(char1, char2)
print(' '.join(result))
