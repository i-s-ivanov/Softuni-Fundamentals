try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print(f'Variable times must be an integer')