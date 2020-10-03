import random

from Breaking_down_integers import int_break
from Breaking_down_integers import counter

from Counting_odd_and_even_numbers import odd
from Counting_odd_and_even_numbers import even
from Counting_odd_and_even_numbers import float_odd
from Counting_odd_and_even_numbers import float_even
from Counting_odd_and_even_numbers import prime_digits

from Sequences_I import seq_a
from Sequences_II import fermat
from Sequences_II import seq_x
from Sequences_II import seq_y

from Print import print_joined_strings
from Print import flip_string_sentence
from Print import print_powers

from Vector_product_tensor_product import vector_prod
from Vector_product_tensor_product import tensor_prod

from Dictionaries import get_me
from Dictionaries import reverse_dict_keys


def exercise_1():
    n = 123456789
    x = 0.123456789

    l = int_break(n)
    k = counter(n)

    print("n =", n)
    print("x =", x)
    print("")

    print("List of integer digits (normal):\n", k)
    print("List of integer digits (reverse):\n", l)


def exercise_2():
    n = 123456789
    x = 0.123456789

    print("n =", n)
    print("x =", x)
    print("")

    print("Number of odd integer digits:\n", odd(n))
    print("Number of even integer digits:\n", even(n))

    print("Number of odd digits after decimal point:\n", float_odd(x))
    print("Number of even digits after decimal point:\n", float_even(x))

    print("Number of prime digits after decimal point:\n", prime_digits(n))


def exercise_3():
    N = random.randint(0, 1e9)

    for n in range(256):
        print(seq_a(N, n))


def exercise_4():
    print("Fermat's last theorem isn't")
    print(fermat(100, 100))
    print("")

    N = random.randint(0, 1e2)

    print(seq_x(N, 1e2))
    print(seq_y(N, 1e2))


def exercise_5():
    print_joined_strings("Hello", "World")
    print("")

    s = "This is sparta!!?!!?!!"
    print(flip_string_sentence(s))
    print("")

    print_powers()
    print("")


def exercise_6():
    a = [1, 0, 0]
    b = [0, 1, 0]
    c = vector_prod(a, b)
    print(c)
    print("")

    a = [1, 2, 3, 4]
    b = [1, 2]
    c = tensor_prod(a, b)

    print("[")
    for i in range(len(c)):
        print(c[i])
    print("]")


def exercise_7():
    get_me()
    print("")

    d = {'alpha': 'a', 'beta': 'b', 'gamma': 'c', 'delta': 'd'}

    print(reverse_dict_keys(d))


def exercise_8():
    import pdb
    pdb.set_trace()


print("")
exercise_1()
# exercise_2()
# exercise_3()
# exercise_4()
# exercise_5()
# exercise_6()
# exercise_7()
# exercise_8()
