def purify(num_list):
    return [i for i in num_list if i % 2 == 0]


def product(int_list):
    p = 1
    for i in int_list:
        p *= i
    return int(p)


def remove_duplicates(lst):
    return list(set(lst))


def remove_duplicates2(lst):
    new = []
    for i in lst:
        if i not in new:
            new.append(i)
    return new


import math


def median(lst):
    s = sorted(lst)
    if len(s) % 2:
        return s[int(math.ceil(len(s) / 2))]
    else:
        return (s[(round(len(s) / 2) - 1)] + s[(round(len(s) / 2))]) / 2.0


def median2(lst):
    s = sorted(lst)
    if len(s) % 2:
        return s[int(math.ceil(len(s) / 2))]
    else:
        return ((s[int(round(len(s) / 2))] + s[int(math.ceil(len(s) / 2))]) / 2.0)


if __name__ == '__main__':
    print(median([4, 5, 5, 4]))
