from under100.day65 import test


def foobar():
    return 2


def test_suite():
    test(foobar() == 2)


if __name__ == '__main__':
    test_suite()
