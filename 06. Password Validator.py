def is_pass_valid(password):
    is_valid_length = False
    is_consist_letters_and_digits = False
    is_got_two_digits = False
    length = len(password)
    if 6 <= length <= 10:
        is_valid_length = True
    else:
        print('Password must be between 6 and 10 characters')

    for ch in password:
        if 'a' <= ch < 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
            is_consist_letters_and_digits = True
        else:
            is_consist_letters_and_digits = False
            break
    if not is_consist_letters_and_digits:
        print('Password must consist only of letters and digits')

    count = 0
    for d in password:
        if '0' <= d <= '9':
            count += 1
    if count >= 2:
        is_got_two_digits = True
    else:
        print('Password must have at least 2 digits')

    if is_valid_length and is_consist_letters_and_digits and is_got_two_digits:
        print('Password is valid')

password = input()

is_pass_valid(password)