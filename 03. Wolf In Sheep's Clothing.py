text = input().split(', ')

for i in range(len(text)):
    if text[i] == "wolf":
        if i == len(text) - 1:
            print(f'Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {len(text) - (i + 1)}! You are about to be eaten by a wolf!')
