people_count = int(input())
cookies_counter = 0
cakes_counter = 0
waffles_counter = 0
total_sum = 0
total_counter = 0

for i in range(people_count):
    name = input()
    kind_of_sweet = input()
    cookies_counter = 0
    cakes_counter = 0
    waffles_counter = 0
    while kind_of_sweet != 'Stop baking!':
        sweets_baked_count = int(input())
        total_counter += int(sweets_baked_count)
        if kind_of_sweet == 'cookies':
            cookies_counter += int(sweets_baked_count)
            total_sum += sweets_baked_count * 1.50
        elif kind_of_sweet == 'cakes':
            cakes_counter += int(sweets_baked_count)
            total_sum += sweets_baked_count * 7.80
        elif kind_of_sweet == 'waffles':
            waffles_counter += int(sweets_baked_count)
            total_sum += sweets_baked_count * 2.30
        kind_of_sweet = input()
    print(f'{name} baked {cookies_counter} cookies, {cakes_counter} cakes and {waffles_counter} waffles.')

print(f'All bakery sold: {total_counter}')
print(f'Total sum for charity: {total_sum:.2f} lv.')
