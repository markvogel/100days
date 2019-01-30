# http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html
# 6.9. Exercises 1-5


import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def seconds_in(a):
    return int((a % 3600) % 60)


def minutes_in(b):
    return int((b % 3600) / 60)


def hours_in(c):
    return int(c / 3600)


def compare(param, param1):
    if param > param1:
        return 1
    if param == param1:
        return 0
    if param < param1:
        return -1


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    # test(hours_in(9010) == 2)
    # test(minutes_in(9010) == 30)
    # test(seconds_in(9010) == 10)
    # test(3 % 4 == 0)
    # test(3 % 4 == 3)
    # test(3 / 4 == 0)
    # test(3 // 4 == 0)
    # test(3 + 4 * 2 == 14)
    # test(4 - 2 + 2 == 0)
    # test(len("hello, world!") == 13)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)


def to_secs(hours_input, minutes_input, seconds_input):
    total_seconds = (hours_input * 3600) + (minutes_input * 60) + seconds_input
    return int(total_seconds)


if __name__ == '__main__':
    test_suite()
