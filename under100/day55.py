# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

import sys
import random


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def add_digits(input_num: int):
    a = [int(i) for i in str(input_num)]
    return sum(a)


# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/ef89s2u
def additive_persistence(a_num, counter=1):
    the_value = sum([int(x) for x in str(a_num)])
    if len(str(the_value)) > 1:
        return additive_persistence(the_value, counter + 1)
    return counter


# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/ef9oa5t
def add_persistence(n, c=1):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s >= 10:
        c += add_persistence(s, c)
    return c


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test((additive_persistence(13)) == 1)
    test((additive_persistence(1234)) == 2)
    test((additive_persistence(9876)) == 2)
    test((additive_persistence(199)) == 3)


def roll_the_dice(roll: str):
    aaa = roll.split('d')
    ccc = [random.randint(1, int(aaa[1])) for _ in range(int(aaa[0]))]
    return sum(ccc)


if __name__ == '__main__':
    # test_suite()
    print(roll_the_dice('5d12'))
    print(roll_the_dice('6d4'))
    print(roll_the_dice('1d2'))
    print(roll_the_dice('1d8'))
    print(roll_the_dice('3d6'))
    print(roll_the_dice('4d20'))
    print(roll_the_dice('100d100'))
