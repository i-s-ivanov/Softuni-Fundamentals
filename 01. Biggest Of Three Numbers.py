first = int(input())
second = int(input())
third = int(input())

if first < second:
    if second < third:
        print(third)
    else:
        print(second)
elif second < first:
    if first < third:
        print(third)
    else:
        print(first)
