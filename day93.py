from day65 import test


def isEvenOrOdd(num):
    if num % 2:
        return "odd"
    return "even"


def minMax(nums):
    if not len(nums):
        return [nums[0], nums[0]]
    return [min(nums), max(nums)]


def sortNumsAscending(a_list):
    if not len(a_list):
        return a_list
    return sorted(a_list)


def test_suite():
    test(isEvenOrOdd(3) == "odd")
    test(isEvenOrOdd(146) == "even")
    test(isEvenOrOdd(19) == "odd")
    test(minMax([1, 2, 3, 4, 5]) == [1, 5])
    test(minMax([2334454, 5]) == [5, 2334454])
    test(minMax([1]) == [1, 1])
    test(sortNumsAscending([1, 2, 10, 50, 5]) == [1, 2, 5, 10, 50])
    test(sortNumsAscending([80, 29, 4, -95, -24, 85]) == [-95, -24, 4, 29, 80, 85])
    test(sortNumsAscending([]) == [])


if __name__ == '__main__':
    test_suite()
