from under100.day65 import test


# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    vowels = "AEIOU"


def tri_area(b, h):
    return (b * h) / 2


def addition(param, param1):
    return param + param1


def addition1(param):
    return param + 1


def divisible_by_five(param):
    return not bool(param % 5)


def test_suite():
    test(tri_area(3, 2) == 3)
    test(tri_area(7, 4) == 14)
    test(tri_area(10, 10) == 50)
    test(addition(3, 2) == 5)
    test(addition(-3, -6) == -9)
    test(addition(7, 3) == 10)
    test(addition1(0) == 1)
    test(addition1(9) == 10)
    test(addition1(-3) == -2)
    test(divisible_by_five(5))
    test(divisible_by_five(-55))
    test(not divisible_by_five(37))


if __name__ == '__main__':
    test_suite()
