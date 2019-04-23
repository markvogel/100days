from under100.day65 import test


# TODO tests all say failed, but 23 looks good
# https://edabit.com/challenge/9CWPv99o4EjZgHnkq
def divide(lst, n):
    new_lst = []
    for i in range(len(lst)):
        if n == sum(lst[:i]) and sum(lst[:i + 1]) > sum(lst[:i]):
            new_lst.append(lst[:i])
            del lst[:i]
        elif len(new_lst) > 1:
            new_lst.append(lst[:i])
            break
    print(new_lst)
    return [new_lst]


def test_suite():
    test((divide([1, 2, 3, 4, 1, 0, 2, 2], 5) == [[1, 2], [3], [4, 1, 0], [2, 2]]))
    test((divide([1, 2, 3, 4, 1, 0, 2, 2], 4) == [[1, 2], [3], [4], [1, 0, 2], [2]]))
    test((divide([1, 3, 2, -1, 2, 1, 1, 3, 1], 3) == [[1], [3], [2, -1, 2], [1, 1], [3], [1]]))
    test((divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 2) == [[1], [2], [2, -1], [2, 0], [1, 0, 1]]))
    test((divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 3) == [[1, 2], [2, -1, 2, 0], [1, 0, 1]]))
    test((divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 5) == [[1, 2, 2, -1], [2, 0, 1, 0, 1]]))
    test((divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3) == [[2, 1, 0, -1, 0, 0], [2, 1], [3]]))
    test((divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 4) == [[2, 1, 0, -1, 0, 0, 2], [1, 3]]))
    test((divide([1, 0, 1, 1, -1, 0, 0], 1) == [[1, 0], [1], [1, -1, 0, 0]]))
    test((divide([1, 0, 1, 1, -1, 0, 0], 2) == [[1, 0, 1], [1, -1, 0, 0]]))
    test((divide([1, 0, 1, 1, -1, 0, 0], 3) == [[1, 0, 1, 1, -1, 0, 0]]))


if __name__ == '__main__':
    test_suite()
