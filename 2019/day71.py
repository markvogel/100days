from under100.day65 import test


def max_end3(nums):
    if nums[0] > nums[-1]:
        return [nums[0] for _ in nums]
    return [nums[-1] for _ in nums]


def make_ends(nums):
    return [nums[0], nums[-1]]


def make_pi():
    return [3, 1, 4]


def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


def sum2(nums):
    return sum(nums[0:2])


def has23(nums):
    return 2 in nums or 3 in nums


def test_suite():
    test(max_end3([1, 2, 3]) == [3, 3, 3])
    test(max_end3([11, 5, 9]) == [11, 11, 11])
    test(max_end3([2, 11, 3]) == [3, 3, 3])
    test(make_ends([1, 2, 3]) == [1, 3])
    test(make_ends([1, 2, 3, 4]) == [1, 4])
    test(make_ends([7, 4, 6, 2]) == [7, 2])
    test(rotate_left3([1, 2, 3]) == [2, 3, 1])
    test(rotate_left3([5, 11, 9]) == [11, 9, 5])
    test(rotate_left3([7, 0, 0]) == [0, 0, 7])
    test(sum2([1, 2, 3]) == 3)
    test(sum2([1, 1]) == 2)
    test(sum2([1, 1, 1, 1]) == 2)
    test(has23([2, 5]))
    test(has23([4, 3]))
    test(not has23([4, 5]))


if __name__ == '__main__':
    test_suite()
