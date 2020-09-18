def to_abs_list(values):
    return [round(x) for x in values]


nums = [float(x) for x in input().split()]
print(to_abs_list(nums))