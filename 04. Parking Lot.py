n = int(input())
parking = set()
for _ in range(n):
    tokens = input().split(", ")
    directions = tokens[0]
    plate_num = tokens[1]
    if directions == "IN":
        parking.add(plate_num)
    elif directions == "OUT":
        parking.remove(plate_num)

if parking:
    [print(x) for x in parking]
else:
    print('Parking Lot is Empty')