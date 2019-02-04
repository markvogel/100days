import sys
import math


def find_factors(a: int):
    factors = []
    x = [i for i in range(1, int(math.sqrt(a) + 1))]
    for each in x:
        if a % each == 0:
            factors.append(each)
    return factors


def smallest(a: int, b: list):
    y = [(a / ii + ii) for ii in b]
    return int(min(y))


def foo(z):
    return smallest(z, find_factors(z))


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test((foo(12)) == 7)
    test((foo(456)) == 43)
    test((foo(4567)) == 4568)
    test((foo(12345)) == 838)
    test((foo(1234567891011)) == 2544788)


if __name__ == '__main__':
    test_suite()
    print(foo(1234567891011))
