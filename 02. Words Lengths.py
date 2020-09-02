line = input().split(', ')
resul = [f'{x} -> {len(x)}' for x in line]
print(', '.join(resul))