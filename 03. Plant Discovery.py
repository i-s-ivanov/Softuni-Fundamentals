n = int(input())
plants_rarity = {}
plants_rating = {}

for _ in range(n):
    data_input = input()
    tokens = data_input.split('<->')
    plant = tokens[0]
    rarity = int(tokens[1])
    if plant not in plants_rarity:
        plants_rarity[plant] = {}
        plants_rarity[plant] = rarity
    else:
        plants_rarity[plant] = rarity

cmd_input = input()
while cmd_input != 'Exhibition':
    args = cmd_input.split(': ')
    cmd = args[0]
    if cmd == 'Rate':
        items = args[1].split(' - ')
        plant = items[0]
        rating = int(items[1])
        if plant in plants_rarity:
            if plant not in plants_rating:
                plants_rating[plant] = []
                plants_rating[plant].append(rating)
            else:
                plants_rating[plant].append(rating)
        else:
            print('error')
    elif cmd == 'Update':
        items = args[1].split(' - ')
        plant = items[0]
        new_rarity = int(items[1])
        if plant in plants_rarity:
            plants_rarity[plant] = new_rarity
        else:
            print('error')
    elif cmd == 'Reset':
        items = args[1].split(' - ')
        plant = items[0]
        if plant in plants_rating:
            plants_rating[plant] = 0.00
        else:
            print('error')

    cmd_input = input()
print(plants_rarity)
print(plants_rating)

sorted_plants_rarity = dict(sorted(plants_rarity.items(), key=lambda x: x[1], reverse=True))
new_dict = {}
for k, v in plants_rating:
    sum = 0
    sum += sum(v[1]) / len(v[1])