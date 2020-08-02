snowballs = int(input())
max_value = 0
snowball_snow_best = ''
snowball_time_best = ''
snowball_quality_best = ''

for i in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value >= max_value:
        max_value = int(snowball_value)
        snowball_snow_best = snowball_snow
        snowball_time_best = snowball_time
        snowball_quality_best = snowball_quality

print(f'{snowball_snow_best} : {snowball_time_best} = {max_value} ({snowball_quality_best})')