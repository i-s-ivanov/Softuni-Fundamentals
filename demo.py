n = int(input())


plants = {}
plants_rating_count = {}

for _ in range(n):
    data = input().split('<->')
    plant = data[0]
    rarity = int(data[1])
    if plant not in plants:
        plants[plant] = [rarity, 0]
        plants_rating_count[plant] = 0
    else:
        plants[plant][0] = rarity



cmd = input()
while cmd != "Exhibition":
    tokens = cmd.split(' ')
    command = tokens[0]
    if command == "Rate:":
        plant = tokens[1]
        if plant in plants:
            rating = float(tokens[3])
            plants[plant][1] += rating
            plants_rating_count[plant] += 1
        else:
            print("error")
    elif command == "Update:":
        plant = tokens[1]
        if plant in plants:
            new_rarity = int(tokens[3])
            plants[plant][0] = new_rarity
        else:
            print("error")
    elif command == "Reset:":
        the_plant = tokens[1]
        if the_plant in plants:
            plants[the_plant][1] = 0
            plants_rating_count[the_plant] = 0
        else:
            print("error")
    else:
        print("error")
    cmd = input()
for key, value in plants_rating_count.items():
    if value == 0:
        plants_rating_count[key] = 1
final_dict = {}

for key, value in plants_rating_count.items():
    for k, val in plants.items():
        for v in range(0, len(val), 2):
            rarity = val[v]
            rating = val[v + 1]
            if k == key:
                average = rating / value
                final_dict[key] = [rarity, average]
final_sorted = dict(sorted(final_dict.items(), key=lambda x: (-x[1][0], -x[1][1])))
print("Plants for the exhibition:")
for key, values in final_sorted.items():
    for value in range(0, len(values), 2):
        print(f"- {key}; Rarity: {values[value]}; Rating: {(values[value + 1]):.2f}")