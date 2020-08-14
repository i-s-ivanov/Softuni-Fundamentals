import re

text = input()
pattern = r'(=|\/)+(?P<place>[A-Z][A-Za-z]{2,})\1'
places = []
matches = re.findall(pattern, text)
if matches:
    for match in matches:
        places.append(match[1])


total = 0
for x in places:
    total += len(x)
print(f'Destinations: {", ".join(places)}')
print(f'Travel Points: {total}')