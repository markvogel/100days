from under100.day65 import test


# https://edabit.com/challenge/QCXxnDHsfF7gtkxze
def mystery_func(n):
    n = str(n)
    r = 1
    for i in n[::-1]:
        r *= int(i)
    return r


def test_suite():
    test(mystery_func(152) == 10)
    test(mystery_func(832) == 48)
    test(mystery_func(19) == 9)
    test(mystery_func(133) == 9)


if __name__ == '__main__':
    test_suite()
