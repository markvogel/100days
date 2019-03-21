from under100.day65 import test
from math import sqrt


def pirates_killed(pirates_gold, inequality):
    for index, gold in enumerate(pirates_gold):
        if abs(gold - max(pirates_gold)) > inequality[index]:
            return True
    return False


def factor_group(num):
    if num == int(sqrt(num)) ** 2:
        return "odd"
    return "even"


def accumulating_product(num_list):
    new = []
    if not len(num_list):
        return new
    new.append(num_list[0])
    for i in range(1, len(num_list)):
        new.append(new[i - 1] * num_list[i])
    return new


def test_suite():
    test(not pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 5]))
    test(pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 1]))
    test(not pirates_killed([3, 3, 10], [7, 7, 0]))
    test(pirates_killed([3, 3, 10], [6, 6, 0]))
    test(not pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 5]))
    test(pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 1]))
    test(not pirates_killed([3, 3, 10], [7, 7, 0]))
    test(pirates_killed([3, 3, 10], [6, 6, 0]))
    test(not pirates_killed([3, 3, 3], [0, 0, 0]))
    test(pirates_killed([3, 3, 4, 4], [0, 0, 1, 1]))
    test(not pirates_killed([3, 3, 4, 4], [1, 1, 0, 0]))
    test(pirates_killed([3, 3, 4, 4], [0, 0, 0, 1]))
    test(pirates_killed([3, 3, 4, 4, 5], [0, 0, 0, 1, 1]))
    test((factor_group(33) == "even"))
    test((factor_group(36) == "odd"))
    test((factor_group(7) == "even"))
    test((factor_group(1) == "odd"))
    test((factor_group(19) == "even"))
    test((factor_group(27) == "even"))
    test((factor_group(100) == "odd"))
    test((factor_group(18) == "even"))
    test((factor_group(16) == "odd"))
    test(accumulating_product([1, 2, 3, 4]) == [1, 2, 6, 24])
    test(accumulating_product([5, 10, 1, 1]) == [5, 50, 50, 50])
    test(accumulating_product([1, 5, 7]) == [1, 5, 35])
    test(accumulating_product([1, 0, 1, 0]) == [1, 0, 0, 0])
    test(accumulating_product([1]) == [1])
    test(accumulating_product([1, 2, 2, 2, 2, 2, 2]) == [1, 2, 4, 8, 16, 32, 64])
    test(accumulating_product([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1])
    test(accumulating_product([]) == [])


if __name__ == '__main__':
    test_suite()
