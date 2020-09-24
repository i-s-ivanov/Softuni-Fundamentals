text = input()
characters_dict = {}

for ch in text:
    if ch not in characters_dict:
        characters_dict[ch] = 0
    characters_dict[ch] += 1

for (k, v) in sorted(characters_dict.items()):
    print(f'{k}: {v} time/s')