from under100.day65 import test


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


def find_digit_amount(num):
    return len(str(num))


def word_rank(string):
    word_list = string.split()
    for word in word_list:
        pass


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
    test(find_digit_amount(123) == 3)
    test(find_digit_amount(56) == 2)
    test(find_digit_amount(7154) == 4)
    test(find_digit_amount(61217311514) == 11)
    test(find_digit_amount(0) == 1)
    test(word_rank("The quick brown fox.") == "brown")
    test(word_rank("Nancy is very pretty.") == "pretty")
    test(word_rank("Check back tomorrow, man!") == "tomorrow")
    test(word_rank("Wednesday is hump day.") == "Wednesday")


if __name__ == '__main__':
    test_suite()
