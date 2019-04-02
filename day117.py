from under100.day65 import test
import itertools


# https://edabit.com/challenge/nT4y8naTzHgknsW6h
def transform_upvotes(a_str):
    a_lst = a_str.split()
    for i in range(len(a_lst)):
        if a_lst[i][-1] == "k":
            a_lst[i] = int(float(a_lst[i][:-1]) * 1000)
        else:
            a_lst[i] = int(a_lst[i])
    return a_lst


# https://edabit.com/challenge/ZsgNrF8jNde4YhmEw
def remove_none(a_list):
    n = a_list.count(None)
    for i in range(n):
        a_list.remove(None)
    return a_list


def combo(lst, n):
    new_lst = []
    if n > len(lst):
        return new_lst
    for i in itertools.combinations(lst, n):
        new_lst.append(list(i))
    return new_lst


def test_suite():
    test(transform_upvotes('20.3k 3.8k 7.7k 992') == [20300, 3800, 7700, 992])
    test(transform_upvotes('5.5k 8.9k 32') == [5500, 8900, 32])
    test(transform_upvotes('6.8k 13.5k') == [6800, 13500])
    test(remove_none(['a', None, 'b', None]) == ['a', 'b'])
    test(remove_none([None, None, None, None, None]) == [])
    test(remove_none([7, 8, None, 9]) == [7, 8, 9])
    test(remove_none([7, None, 8, None, 9]) == [7, 8, 9])
    test(combo([1, 2, 3, 4], 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    test(combo([1, 2, 3, 4], 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])
    test(combo([1, 2, 3, 4], 1) == [[1], [2], [3], [4]])
    test(combo([1, 2, 3, 4], 5) == [])
    test(combo([1, 2, 3, 4], 0) == [[]])
    test(combo(['a', 'b', 'c'], 0) == [[]])
    test(combo(['a', 'b', 'c'], 4) == [])
    test(combo(['a', 'b', 'c'], 1) == [['a'], ['b'], ['c']])
    test(combo(['a', 'b', 'c'], 2) == [['a', 'b'], ['a', 'c'], ['b', 'c']])
    test(combo(['a', 'b', 'c'], 3) == [['a', 'b', 'c']])


if __name__ == '__main__':
    test_suite()
