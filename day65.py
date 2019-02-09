import sys


# https://codingbat.com/prob/p173401
def sleep_in(weekday, vacation):
    if not weekday and not vacation:
        return True
    if vacation:
        return True
    if weekday:
        return False


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# https://codingbat.com/prob/p120546
def monkey_trouble(a_smile, b_smile):
    # if a_smile and b_smile:
    #     return True
    # if not a_smile and not b_smile:
    #     return True
    # return False
    return a_smile == b_smile


# https://codingbat.com/prob/p141905
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    return a + b


# https://codingbat.com/prob/p197466
def diff21(n):
    if n > 21:
        return abs(21 - n) * 2
    return abs(n - 21)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sleep_in(False, False))
    test(not sleep_in(True, False))
    test(sleep_in(False, True))
    test(sleep_in(True, True))
    test(monkey_trouble(True, True))
    test(monkey_trouble(False, False))
    test(not monkey_trouble(True, False))
    test(not monkey_trouble(False, True))
    test(sum_double(1, 2) == 3)
    test(sum_double(3, 2) == 5)
    test(sum_double(2, 2) == 8)
    test(diff21(19) == 2)
    test(diff21(10) == 11)
    test(diff21(21) == 0)


if __name__ == '__main__':
    test_suite()
