from under100.day65 import test
from pprint import pprint
from random import randint
from collections import defaultdict


# https://codingbat.com/prob/p166884
def parrot_trouble(talking, hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
    return False


# https://codingbat.com/prob/p124984
def makes10(a, b):
    if a == 10 or b == 10 or (a + b) == 10:
        return True
    return False


objects = [randint(0, 50) for _ in range(500)]
pprint(objects)


# objects = ['a','b','a','c','a','b']


def foo(iterable):
    ret = defaultdict(list)
    for index, o in enumerate(iterable):
        ret[o].append(index)
    return ret


locations = foo(objects)

duplicates = {item: indexes for item, indexes in locations.items() if len(indexes) > 1}

pprint(duplicates)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(parrot_trouble(True, 6))
    test(not parrot_trouble(True, 7))
    test(not parrot_trouble(False, 6))
    test(parrot_trouble(True, 21))
    test(not parrot_trouble(False, 21))
    test(not parrot_trouble(False, 20))
    test(parrot_trouble(True, 23))
    test(not parrot_trouble(False, 23))
    test(not parrot_trouble(True, 20))
    test(not parrot_trouble(False, 12))
    test(makes10(9, 10))
    test(not makes10(9, 9))
    test(makes10(1, 9))


if __name__ == '__main__':
    test_suite()
