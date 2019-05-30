import random


# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
def list_less_than_ten(lst):
    for num in lst:
        if num < 5:
            print(num)


def list_less_than_ten2(lst):
    b = [i for i in lst if i < 5]
    print(b)


def list_less_than_ten3(lst):
    c = int(input("Please enter a number: "))
    b = [i for i in lst if i < c]
    print(b)


# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
def divisors():
    num = int(input("Please enter a number: "))
    num_range = [i for i in range(1, num)]
    d = [i for i in num_range if not num % i]
    print(d)


# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
def list_overlap(lst1, lst2):
    lst3 = set([i for i in lst1 if i in lst2])
    print(lst3)


# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
def string_lists(str1):
    return str1.lower() == (str1.lower())[::-1]


if __name__ == '__main__':
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # list_less_than_ten3(a)
    # divisors()
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # a = [i for i in range(1, random.randint(1, 10))]
    # b = [i for i in range(1, random.randint(1, 100))]
    #
    # list_overlap(a, b)
    print(string_lists("Racecar"))
