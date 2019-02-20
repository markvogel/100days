from day65 import test


def count_evens(nums):
    count = 0
    for i in nums:
        if not i % 2:
            count += 1
    return count


def sum13(nums):
    if not len(nums):
        return 0
    sum = 0
    for c, i in enumerate(nums):
        if i == 13:
            try:
                nums[c + 1] = 0
            except IndexError:
                continue
            continue
        sum += i
    return sum


def big_diff(nums):
    return max(nums) - min(nums)


def sum67(nums):
    if not len(nums):
        return 0
    for i in range(len(nums)):
        if nums[i] == 6:
            pass
    return sum(nums)


def test_suite():
    test(count_evens([2, 1, 2, 3, 4]) == 3)
    test(count_evens([2, 2, 0]) == 3)
    test(count_evens([1, 3, 5]) == 0)
    test(sum13([1, 2, 2, 1]) == 6)
    test(sum13([1, 1]) == 2)
    test(sum13([1, 2, 2, 1, 13]) == 6)
    test(sum13([1, 2, 2, 1]) == 6)
    test(sum13([1, 1]) == 2)
    test(sum13([1, 2, 2, 1, 13]) == 6)
    test(sum13([1, 2, 13, 2, 1, 13]) == 4)
    test(sum13([13, 1, 2, 13, 2, 1, 13]) == 3)
    test(sum13([]) == 0)
    test(sum13([13]) == 0)
    test(sum13([13, 13]) == 0)
    test(sum13([13, 0, 13]) == 0)
    test(sum13([13, 1, 13]) == 0)
    test(sum13([5, 7, 2]) == 14)
    test(sum13([5, 13, 2]) == 5)
    test(sum13([0]) == 0)
    test(sum13([13, 0]) == 0)
    test(big_diff([10, 3, 5, 6]) == 7)
    test(big_diff([7, 2, 10, 9]) == 8)
    test(big_diff([2, 10, 7, 2]) == 8)
    test(sum67([1, 2, 2]) == 5)
    test(sum67([1, 2, 2, 6, 99, 99, 7]) == 5)
    test(sum67([1, 1, 6, 7, 2]) == 4)


if __name__ == '__main__':
    test_suite()
