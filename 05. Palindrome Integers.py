def is_palindrome(a):
    for num in st:
        reversed_num = num[::-1]
        if num == reversed_num:
            print('True')
        else:
            print('False')


st = input().split(', ')

is_palindrome(st)