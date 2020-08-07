resource = input()
my_dict = {}

while resource != 'stop':
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = 0
    my_dict[resource] += quantity
    resource = input()

for k, v in my_dict.items():
    print(f'{k} -> {v}')