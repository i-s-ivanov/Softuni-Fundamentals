tokens = list(map(int, input().split()))
n = tokens[0]
m = tokens[1]

set_n = set()
set_m = set()

for _ in range(n):
    num = int(input())
    set_n.add(num)

for _ in range(m):
    num = int(input())
    set_m.add(num)

intersection = set_n & set_m
for number in intersection:
    print(number)
