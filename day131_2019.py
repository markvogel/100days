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


def test_suite():
    pass


if __name__ == '__main__':
    foo(24)
