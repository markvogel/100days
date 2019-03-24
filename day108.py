from under100.day65 import test


# https://edabit.com/challenge/RixixSPn6psQKYpnP
def mystery_func(a_list, num):
    return [i % num for i in a_list]


def intersection_union(num_list1, num_list2):
    intersection = sorted([i for i in set(num_list1) if i in set(num_list2)])
    union = list(num_list1)
    for i in num_list2:
        union.append(i)
    union = sorted(list(set(union)))
    return [intersection, union]


def test_suite():
    test(mystery_func([5, 7, 8, 2, 1], 2) == [1, 1, 0, 0, 1])
    test(mystery_func([9, 8, 16, 47], 4) == [1, 0, 0, 3])
    test(mystery_func([17, 11, 99, 55, 23, 1], 5) == [2, 1, 4, 0, 3, 1])
    test(mystery_func([6, 1], 7) == [6, 1])
    test(mystery_func([3, 2, 9], 3) == [0, 2, 0])
    test(mystery_func([48, 22, 0, 19, 33, 100], 10) == [8, 2, 0, 9, 3, 0])
    test(intersection_union([1, 2, 3, 4, 4], [4, 5, 9]) == [[4], [1, 2, 3, 4, 5, 9]])
    test(intersection_union([1, 2, 3], [4, 5, 6]) == [[], [1, 2, 3, 4, 5, 6]])
    test(intersection_union([1, 1], [1, 1, 1, 1]) == [[1], [1]])
    test(intersection_union([5, 5], [5, 6]) == [[5], [5, 6]])
    test(intersection_union([7, 8, 9, 6], [9, 7, 6, 8]) == [[6, 7, 8, 9], [6, 7, 8, 9]])
    test(intersection_union([4, 1, 1, 2], [1, 4, 4, 4, 4, 4, 4]) == [[1, 4], [1, 2, 4]])


if __name__ == '__main__':
    test_suite()
