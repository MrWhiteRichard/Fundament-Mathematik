def print_joined_strings(st1, st2):
    s = st1 + st2
    print(s)


def flip_string_sentence(s):
    sentence = s.split()
    first_word = sentence[0]
    last_word = sentence[-1]

    possible_endings = ['.', '!', '?']
    e_counter = len(last_word) - 1
    ending = ""

    while last_word[e_counter] in possible_endings:
        ending += last_word[e_counter]
        e_counter -= 1

    last_word = last_word[0:e_counter+1]

    last_word = last_word[0].upper() + last_word[1:-1] + last_word[-1]
    first_word = first_word[0].lower() + first_word[1:-1] + first_word[-1]

    s_new = last_word

    for i in range(1, len(sentence)-1):
        s_new += ' ' + sentence[i]

    s_new += ' ' + first_word + ending[::-1]

    return s_new


def print_powers():
    dash = 16 * '-'

    print(dash)
    print('{:>3} {:>4} {:>5}'.format('n', 'n^2', 'n^3'))
    print(dash)

    for i in range(1, 11):
        i_1 = '{:>3}'.format(i)
        i_2 = '{:>4}'.format(i**2)
        i_3 = '{:>5}'.format(i**3)
        print(i_1, i_2, i_3)

    print(dash)
