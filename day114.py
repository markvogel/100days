from under100.day65 import test


def number_args(*args):
    return len(args)


def isTruthy(param):
    return int(bool(param))


def remainder(param, param1):
    return param % param1


def test_suite():
    test(number_args("a", "b", "c") == 3)
    test(number_args(10, 20, 30, 40, 50) == 5)
    test(number_args("x", "y") == 2)
    test(number_args() == 0)
    test(isTruthy(0) == 0)
    test(isTruthy(False) == 0)
    test(isTruthy("") == 0)
    test(isTruthy("false") == 1)
    test(remainder(1, 3) == 1)
    test(remainder(-9, 45) == 36)
    test(remainder(5, 5) == 0)


if __name__ == '__main__':
    test_suite()
