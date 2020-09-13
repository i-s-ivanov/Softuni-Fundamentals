text = input()
result = [x for x in text if x not in ['a', 'o', 'e', 'i', 'u']]
print(''.join(result))