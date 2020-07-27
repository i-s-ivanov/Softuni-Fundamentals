budget = float(input())
floor_price = float(input())

pack_eggs_price = floor_price * 0.75
milk_price = (floor_price * 1.25) / 4
price_per_cozunak = floor_price + pack_eggs_price + milk_price
counter = 0
coloured_eggs = 0

while budget >= price_per_cozunak:
    counter += 1
    budget -= price_per_cozunak
    coloured_eggs += 3
    if counter % 3 == 0:
        coloured_eggs -= counter - 2

print(f'You made {counter} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')