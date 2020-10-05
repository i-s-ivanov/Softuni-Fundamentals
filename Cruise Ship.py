cruise_type = input()
room_type = input()
nights = int(input())
price = 0

if cruise_type == 'Mediterranean':
    if room_type == 'standard cabin':
        price = nights * 27.50
    elif room_type == 'cabin with balcony':
        price = nights * 30.20
    elif room_type == 'apartment':
        price = nights * 40.50

elif cruise_type == 'Adriatic':
    if room_type == 'standard cabin':
        price = nights * 22.99
    elif room_type == 'cabin with balcony':
        price = nights * 25.00
    elif room_type == 'apartment':
        price = nights * 34.99

elif cruise_type == 'Aegean':
    if room_type == 'standard cabin':
        price = nights * 23.00
    elif room_type == 'cabin with balcony':
        price = nights * 26.60
    elif room_type == 'apartment':
        price = nights * 39.80

if nights > 7:
    price = price - price * 0.25

price = price * 4
print(f'Annie\'s holiday in the {cruise_type} sea costs {price:.2f} lv.')