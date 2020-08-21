def loading_bar(number):
    bar = []
    num = number // 10
    bar.append('%' * num)
    left = 10 - num
    if left == 0:
        bar = ''.join(bar)
        print('100% Complete!')
        print(f'[{bar}]')
    else:
        bar.append('.' * left)
        bar = ''.join(bar)
        print(f'{number}% [{bar}]')
        print('Still loading...')

number = int(input())

loading_bar(number)