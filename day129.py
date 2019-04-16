from under100.day65 import test


# https://edabit.com/challenge/zYr4v5gb43kJPje9g
def moving_partition(lst):
    new = []
    for i in range(1, len(lst)):
        new.append([lst[:i], lst[i:]])
    return new


def test_suite():
    test(moving_partition([-1, -1, -1, -1])
         == [[[-1], [-1, -1, -1]], [[-1, -1], [-1, -1]], [[-1, -1, -1], [-1]]])
    test(moving_partition([1, 2, 3, 4, 5])
         == [[[1], [2, 3, 4, 5]], [[1, 2], [3, 4, 5]], [[1, 2, 3], [4, 5]], [[1, 2, 3, 4], [5]]])
    test(moving_partition([]) == [])
    test(moving_partition([8, 9, 10]) == [[[8], [9, 10]], [[8, 9], [10]]])


if __name__ == '__main__':
    test_suite()
