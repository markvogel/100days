from under100.day65 import test


# https://edabit.com/challenge/KKmM4ob5wwPwf8kgS
def get_frequencies(lst):
    return {key: lst.count(key) for key in lst}


# https://edabit.com/challenge/ud5FBjsdGApJhJMtm
def check_all_even(lst):
    x = [((i % 2) == 0) for i in lst]
    return all(x)


def test_suite():
    test(get_frequencies(['A', 'B', 'A', 'A', 'A']) == {'A': 4, 'B': 1})
    test(get_frequencies([1, 2, 3, 3, 2]) == {1: 1, 2: 2, 3: 2})
    test(get_frequencies([True, False, True, False, False]) == {True: 2, False: 3})
    test(get_frequencies([]) == {})
    test(not check_all_even([1, 2, 3, 4]))
    test(check_all_even([2, 4, 6]))
    test(not check_all_even([5, 6, 8, 10]))
    test(check_all_even([-2, 2, -2, 2]))


if __name__ == '__main__':
    test_suite()
