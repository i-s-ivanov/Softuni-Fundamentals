text = input()
name_price_dict = {}
name_quantity_dict = {}

while text != 'buy':
    tokens = text.split()
    item = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    if item not in name_price_dict:
        name_price_dict[item] = 0
    name_price_dict[item] = price
    if item not in name_quantity_dict:
        name_quantity_dict[item] = 0
    name_quantity_dict[item] += quantity
    text = input()

for k in name_price_dict:
    print(f'{k} -> {(name_price_dict[k] * name_quantity_dict[k]):.2f}')
