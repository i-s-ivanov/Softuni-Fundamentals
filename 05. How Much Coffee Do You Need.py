command = input()
coffees = 0
lowers = ['dog', 'cat', 'coding', 'movie']
uppers = ['DOG', 'CAT', 'CODING', 'MOVIE']

while command != 'END':
    if command in lowers:
        coffees += 1
    elif command in uppers:
        coffees += 2
    command = input()
if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')