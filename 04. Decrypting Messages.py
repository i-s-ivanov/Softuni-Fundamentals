key = int(input())
n = int(input())
message = ''

for i in range(n):
    char = input()
    ascii_num = ord(char)
    new_char = chr(ascii_num + key)
    message += new_char

print(message)