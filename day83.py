from day65 import test
import re


def mult_table(nums):
    print(f"".rjust(3), end='')
    for num in nums:
        print(f"{num}".rjust(5), end='')
    print("\n", end='')
    print(" :" + "-" * 61)
    for num in nums:
        print(f"{num}:".rjust(3), end='')
        for i in range(len(nums)):
            print(f"{num * (i + 1)}".rjust(5), end='')
            if i == len(nums) - 1:
                print('\n', end='')


def reverse(param):
    return param[::-1]


def mirror(param):
    return param + param[::-1]


def remove_letter(param, param1):
    return param1.replace(param, '')


def is_palindrome(param):
    return param == param[::-1]


# need to fix this so that the tests pass, currently if the substrings overlap, it doesn't work
def count(param, param1):
    return param1.count(param)


def remove(param, param1):
    return param1.replace(param, '', 1)


def remove_all(param, param1):
    return param1.replace(param, '')


def test_suite():
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    # test(is_palindrome(""))  # Is an empty string a palindrome?
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")


if __name__ == '__main__':
    # nums = [i + 1 for i in range(12)]
    # mult_table(nums)
    test_suite()
