from under100.day65 import test


def ltr_dict():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_dict = {num + 1: letter for num, letter in enumerate(letters)}
    return letter_dict


# https://edabit.com/challenge/tRHaoWNaHBJCYD5Nx
def same_letter_pattern(s1, s2):
    pass


# https://edabit.com/challenge/QCXxnDHsfF7gtkxze
def mystery_func(num):
    num = str(num)[::-1]
    num_list = [int(i) for i in num]
    rtn = 1
    for i in num_list:
        rtn *= i
    return rtn


def test_suite():
    # test(same_letter_pattern('ABAB', 'CDCD'))
    # test(same_letter_pattern('AAABBB', 'CCCDDD'))
    # test(same_letter_pattern('ABCBA', 'BCDCB'))
    # test(same_letter_pattern('AAAA', 'BBBB'))
    # test(same_letter_pattern('BAAB', 'ABBA'))
    # test(same_letter_pattern('BAAB', 'QZZQ'))
    # test(same_letter_pattern('TTZZVV', 'PPSSBB'))
    # test(same_letter_pattern('ZYX', 'ABC'))
    # test(same_letter_pattern('AABAA', 'SSCSS'))
    # test(same_letter_pattern('AABAABAA', 'SSCSSCSS'))
    # test(same_letter_pattern('UBUBUBUB', 'WEWEWEWE'))
    # test(not same_letter_pattern('FFGG', 'FFG'))
    # test(not same_letter_pattern('FFGG', 'CDCD'))
    # test(not same_letter_pattern('FFFG', 'GGHI'))
    # test(not same_letter_pattern('FFFF', 'ABCD'))
    # test(not same_letter_pattern('ABCA', 'ABCD'))
    # test(not same_letter_pattern('ABCAAA', 'DDABCD'))
    test(mystery_func(152) == 10)
    test(mystery_func(832) == 48)
    test(mystery_func(5511) == 25)
    test(mystery_func(19) == 9)
    test(mystery_func(133) == 9)


if __name__ == '__main__':
    test_suite()
