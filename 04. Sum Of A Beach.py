text = input().lower()
counter = 0

counter += text.count("sand")
counter += text.count("sun")
counter += text.count('water')
counter += text.count('fish')

print(counter)