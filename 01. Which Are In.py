words = input().split(', ')
string = input()


res = [word for word in words if word in string]

print(res)

