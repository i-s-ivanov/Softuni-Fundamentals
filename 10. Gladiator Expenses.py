lost_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total = 0
shield_counter = 0

for i in range(1, lost_count + 1):
    if i % 2 == 0:
        total += helmet_price
    if i % 3 == 0:
        total += sword_price
    if i % 2 == 0 and i % 3 == 0:
        total += shield_price
        shield_counter += 1
    if shield_counter > 0:
        if shield_counter % 2 == 0:
            total += armor_price
            shield_counter = 0

print(f'Gladiator expenses: {total:.2f} aureus')