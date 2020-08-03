n = int(input())
is_special = False

for i in range(1, n + 1):
    st = str(i)
    sum = 0
    for ch in st:
        sum += int(ch)
    if sum == 5 or sum == 7 or sum == 11:
        is_special = True
    else:
        is_special = False
    print(f'{i} -> {is_special}')