flight = input()
min_waiting = 600
hours = 0

while flight != 'End':
    price = float(input())
    waiting = int(input())
    if waiting < min_waiting:
        min_waiting = waiting
        chosen_flight = flight
        chosen_price = price
    flight = input()

price_lv = chosen_price * 1.96
while min_waiting >= 60:
    hours += 1
    min_waiting = min_waiting - 60

print(f'Ticket found for flight {chosen_flight} costs {price_lv:.2f} leva with {hours}h {min_waiting}m stay')