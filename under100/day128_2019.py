from under100.day65 import test
from collections import defaultdict
import random


def foo():
    a = ["a", "b", "c", "d", "e", "f", "g"]
    d = defaultdict(lambda: 6)
    d["k"] += 1
    for i in a:
        d[i] = 1 + random.randint(1, 10)
    d["k"] = 233
    print(d["k"])
    print(d.items())


def test_suite():
    pass


if __name__ == '__main__':
    test_suite()
    foo()
