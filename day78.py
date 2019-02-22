from day65 import test
import math


def compare(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def slope(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)


def intercept(x1, y1, x2, y2):
    # y = mx + b
    # b = y-mx
    m = slope(x1, y1, x2, y2)
    return y1 - m * x1


def is_even(n):
    if not n % 2:
        return True
    return False


def is_odd(n):
    return not is_even(n)


def is_factor(f, n):
    if n % f:
        return False
    return True


def is_multiple(param, param1):
    pass


def test_suite():
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(2))
    test(is_even(200))
    test(not is_even(-11))
    test(is_odd(1))
    test(is_odd(111))
    test(not is_odd(22))
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))


if __name__ == '__main__':
    test_suite()
