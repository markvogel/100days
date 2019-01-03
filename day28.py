import random


# https://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html

def default_app():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(set(a).intersection(b))

    # this works, but doesn't feel right
    c = [x for x in a and b if x in a and x in b]

    print(c)


def extra_app():
    r1 = [random.randint(0, 10) for i in range(10)]
    r2 = [random.randint(0, 10) for i in range(10)]
    return [i for i in r1 if i in r2]


if __name__ == '__main__':
    # print(extra_app())
    default_app()
