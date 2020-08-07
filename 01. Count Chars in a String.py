def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        my_dict[ch] = 0

text = input()

my_dict = {}

for ch in text:
    if ch == ' ':
        continue
    validate_key_existing(my_dict, ch)
    my_dict[ch] += 1

for k, v in my_dict.items():
    print(f'{k} -> {v}')