from under100.day65 import test
from datetime import datetime

day_of_year = datetime.now().timetuple().tm_yday


# https://www.hackerrank.com/challenges/py-if-else/problem
def foo(n):
    if not n % 2:
        if n in range(2, 6):
            print("Not Weird")
        if n in range(6, 21):
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")


# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(y):
    if by_4(y):
        if by_100(y):
            return by_400(y)
        return by_100(y)
    return by_4(y)


def by_4(n):
    return not n % 4


def by_100(n):
    return not n % 100


def by_400(n):
    return not n % 400


def test_suite():
    pass


if __name__ == '__main__':
    print(is_leap(1800))
    print(is_leap(2400))
