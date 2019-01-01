# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def list_overlap(list1, list2):
    return [i for i in list1 if i in list2]


def create_random_list():
    return [random.randint(1, 10) for _ in range(100)]


if __name__ == '__main__':
    print(list_overlap(create_random_list(), create_random_list()))
