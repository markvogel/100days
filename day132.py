from under100.day65 import test
import math


# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-1.php
def pow2(a_num):
    a = [i ** 2 for i in range(1000) if not (i % 2)]
    print(a)
    return a_num in a


def pow2_2(a_num):
    return a_num > 0 and (a_num & (a_num - 1)) == 0


def test_suite():
    test(pow2_2(2))
    test(not pow2_2(49))
    test(not pow2_2(151))
    test(not pow2_2(48))
    test(pow2_2(4))
    test(pow2_2(8))
    test(pow2_2(16))
    test(pow2_2(32))
    test(pow2_2(64))


if __name__ == '__main__':
    test_suite()
