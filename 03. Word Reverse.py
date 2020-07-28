word = input()
length = len(word)
reversed_word = ''
for char in range(length - 1, -1, -1):
    reversed_word += word[char]

print(reversed_word)