from under100.day65 import test


# https://edabit.com/challenge/RixixSPn6psQKYpnP
def mystery_func(a_list, num):
    return [i % num for i in a_list]


def test_suite():
    test(mystery_func([5, 7, 8, 2, 1], 2) == [1, 1, 0, 0, 1])
    test(mystery_func([9, 8, 16, 47], 4) == [1, 0, 0, 3])
    test(mystery_func([17, 11, 99, 55, 23, 1], 5) == [2, 1, 4, 0, 3, 1])
    test(mystery_func([6, 1], 7) == [6, 1])
    test(mystery_func([3, 2, 9], 3) == [0, 2, 0])
    test(mystery_func([48, 22, 0, 19, 33, 100], 10) == [8, 2, 0, 9, 3, 0])


if __name__ == '__main__':
    test_suite()
