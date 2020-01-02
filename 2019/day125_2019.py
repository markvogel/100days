from under100.day65 import test


def list_ends(list1):
    return [list1[0], list1[-1]]


def test_suite():
    test(list_ends([5, 10, 15, 20, 25]) == [5, 25])


if __name__ == '__main__':
    test_suite()
