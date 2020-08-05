n = int(input())
opened = False
closed = False

for i in range(n):
    sym = input()
    if sym == '(':
        if opened:
            break
        opened = True
    elif sym == ')':
        if opened:
            closed = True
        else:
            break

if opened and closed:
    print("BALANCED")
else:
    print('UNBALANCED')
