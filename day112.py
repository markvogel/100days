from under100.day65 import test
import numpy as np

array1 = [i for i in range(10)]
array2 = [i for i in range(100, 200, 10)]
array3 = [i for i in "hello"]


# https://edabit.com/challenge/woA74HtrheoQva87R
def concat(*args):
    args_joined = []
    for i in args:
        args_joined.extend(i)
    return args_joined


def test_suite():
    test(concat([1, 2, 3], [4, 5], [6, 7]) == [1, 2, 3, 4, 5, 6, 7])
    test(concat([1], [2], [3], [4], [5], [6], [7]) == [1, 2, 3, 4, 5, 6, 7])
    test(concat([1, 2], [3, 4]) == [1, 2, 3, 4])
    test(concat([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4])
    test(concat(['a'], ['b', 'c']) == ['a', 'b', 'c'])


if __name__ == '__main__':
    test_suite()
    # a, b = np.array(array1), np.array(array2)
    # c = np.array(array3)
    # print(a + b)
    # print(c + c)
