def int_to_string(word):
    word = list(word)
    num_str = ''
    while True:
        if not word[0].isdigit():
            break
        num_str += word[0]
        word.pop(0)
    num = int(num_str)
    word.insert(0, chr(num))
    return ''.join(word)


def switch_letters(word):
    chars_list = list(word)
    chars_list[1], chars_list[-1] = chars_list[-1], chars_list[1]
    return ''.join(chars_list)


def decrypt_word(word):
    word = int_to_string(word)
    word = switch_letters(word)
    return word


words = input().split()
words_list = [decrypt_word(word) for word in words]
print(' '.join(words_list))
