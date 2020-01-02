import random


# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
def list_overlap_comprehensions(list1, list2):
    return [i for i in list2 if i in set(list1)]


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [random.randint(1, 100) for i in range(20)]
    d = [random.randint(1, 100) for i in range(20)]
    # print(c, d)
    print(list_overlap_comprehensions(c, d))
