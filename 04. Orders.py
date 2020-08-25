def total_price(product, quantity):
    result = None
    if product == 'coffee':
        result = quantity * 1.50
    elif product == 'water':
        result = quantity * 1
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'snacks':
        result = quantity * 2
    return result


product = input()
quantity = int(input())

print(f'{total_price(product, quantity):.2f}')
