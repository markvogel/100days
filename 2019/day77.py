from under100.day65 import test


def sum67(nums):
    if not len(nums):
        return 0
    for i in range(len(nums)):
        if 6 in nums:
            del nums[nums.index(6):nums.index(7) + 1]
    return sum(nums)


def centered_average(nums):
    nums.remove(min(nums))
    nums.remove(max(nums))
    return sum(nums) // len(nums)


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


def test_suite():
    test(sum67([1, 2, 2]) == 5)
    test(sum67([1, 2, 2, 6, 99, 99, 7]) == 5)
    test(sum67([1, 1, 6, 7, 2]) == 4)
    test(centered_average([1, 2, 3, 4, 100]) == 3)
    test(centered_average([1, 1, 5, 5, 10, 8, 7]) == 5)
    test(centered_average([-10, -4, -2, -4, -2, 0]) == -3)
    test(has22([1, 2, 2]))
    test(not has22([1, 2, 1, 2]))
    test(not has22([2, 1, 2]))


if __name__ == '__main__':
    test_suite()
