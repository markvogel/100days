from under100.day65 import test
import numpy as np


# https://edabit.com/challenge/GaJkMnuHLuPmXZK7h
def letters(a_str1, a_str2):
    lst1, lst2 = [i for i in a_str1], [i for i in a_str2]
    lst1_set, lst2_set = set(lst1), set(lst2)
    shared, u1, u2 = [], [], []
    for i in lst1_set:
        if i in a_str2:
            shared.append(i)
        else:
            u1.append(i)
    for i in lst2_set:
        if i not in a_str1:
            u2.append(i)
    return [sort_join(shared), sort_join(u1), sort_join(u2)]


def sort_join(lst):
    return "".join(sorted(lst))


# https://edabit.com/challenge/ucsJxQNrkYnpzPaFj
def char_appears(a_str, ch):
    return [i.count(ch) for i in a_str.lower().split()]


# https://edabit.com/challenge/pboAYDuTv7ziJgtxC
def min_turns(str1, str2):
    num1, num2 = [int(i) for i in str1], [int(i) for i in str2]
    diff = [abs(num1[i] - num2[i]) for i in range(len(num1))]
    return sum(diff)


def test_suite():
    test(letters("sharp", "soap") == ["aps", "hr", "o"])
    test(letters("board", "bored") == ["bdor", "a", "e"])
    test(letters("happiness", "envelope") == ["enp", "ahis", "lov"])
    test(letters("match", "ham") == ["ahm", "ct", ""])
    test(letters("kerfuffle", "fluffy") == ["flu", "ekr", "y"])
    test(char_appears("She sells sea shells by the seashore.", "s") == [1, 2, 1, 2, 0, 0, 2])
    test(char_appears("Peter Piper picked a peck of pickled peppers.", "p") == [1, 2, 1, 0, 1, 0, 1, 3])
    test(char_appears("She hiked in the morning, then swam in the river.", "t") ==
         [0, 0, 0, 1, 0, 1, 0, 0, 1, 0])
    test(char_appears("I scream, you scream, we all scream for ice cream.", "f") ==
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    test(char_appears("Snap, crackle, pop!", "p") == [1, 0, 2])
    test(char_appears("What a wonderful world.", "w") == [1, 0, 1, 1])
    test(min_turns("4089", "5672") == 9)
    test(min_turns("1732", "4444") == 9)
    test(min_turns("7109", "2332") == 13)
    test(min_turns("2391", "4984") == 10)
    test(min_turns("1234", "3456") == 8)
    test(min_turns("1111", "1100") == 2)
    test(min_turns("1111", "0000") == 4)
    test(min_turns("0000", "9999") == 4)


if __name__ == '__main__':
    test_suite()
