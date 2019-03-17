import math


def diameter(radius):
    return r2(2 * radius)


def circumference(radius):
    return r2(2 * math.pi * radius)


def area(radius):
    return r2(math.pi * radius ** 2)


def r2(value):
    return round(value, 2)


if __name__ == '__main__':
    radius = 6.75
    d, c, a = diameter(radius), circumference(radius), area(radius)
    print(d)
    print(c)
    print(a)
