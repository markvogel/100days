from under100.day65 import test


# https://edabit.com/challenge/dEokmCfykvXgcJ3pi
def first_arg(*args):
    if not args:
        return None
    return args[0]


def last_arg(*args):
    if not args:
        return None
    return args[-1]


# https://edabit.com/challenge/czjjch48tZYjTDmtH
def is_shifted(lst1, lst2):
    if sum(lst1) == 0:
        return True


def is_multiplied(lst1, lst2):
    if sum(lst1) == 0:
        return True


def test_suite():
    test(first_arg(1, 2, 3) == 1)
    test(first_arg('a', 'b', 'c') == 'a')
    test(first_arg(8) == 8)
    test(first_arg() is None)
    test(last_arg(1, 2, 3) == 3)
    test(last_arg('a', 'b', 'c') == 'c')
    test(last_arg(8) == 8)
    test(last_arg() is None)
    test(is_shifted([1, 2, 3], [2, 3, 4]))
    test(is_shifted([1, 2, 3], [-9, -8, -7]))
    test(is_multiplied([1, 2, 3], [10, 20, 30]))
    test(is_multiplied([1, 2, 3], [-0.5, -1, -1.5]))
    test(is_multiplied([1, 2, 3], [0, 0, 0]))
    test(not is_shifted([1, 2, 3], [2, 3, 5]))
    test(not is_shifted([1, 2, 3], [-9, -1, -7]))
    test(not is_multiplied([1, 2, 3], [10, 20, 29]))
    test(not is_multiplied([1, 2, 3], [-0.5, -1, -2]))
    test(not is_multiplied([1, 2, 3], [0, 0, 1]))


if __name__ == '__main__':
    test_suite()
