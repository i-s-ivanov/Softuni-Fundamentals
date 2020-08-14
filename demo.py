n = int(input())
dict = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(synonym)

for word in dict:
    print(f'{word} - {", ".join(dict[word])}')
