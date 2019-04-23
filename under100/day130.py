from under100.day65 import test


# https://edabit.com/challenge/vfTJHRxAGeMxkvxni
def count_overlapping(intervals, point):
    count = 0
    for i in intervals:
        # a = [i for i in range(i[0], i[1] + 1)]
        # if point in a:
        #     count += 1
        if i[0] <= point <= i[1]:
            count += 1
    return count


def in_box(lst):
    return "*" in "".join(lst)


def multiplicity(lst):
    a = set(lst)
    print(a)
    r = []
    for i in a:
        r.append([i, lst.count(i)])
    print(r)
    return r


def test_suite():
    test(multiplicity([1, 1, 1, 2, 2, 3]) == [[1, 3], [2, 2], [3, 1]])
    test(multiplicity([1, 1, 1, 1, 1]) == [[1, 5]])
    test(multiplicity([1, 5, 4, 3, 2]) == [[1, 1], [5, 1], [4, 1], [3, 1], [2, 1]])
    test(count_overlapping([[1, 2], [2, 3], [3, 4]], 5) == 0)
    test(count_overlapping([[1, 2], [5, 6], [5, 7]], 5) == 2)
    test(count_overlapping([[1, 2], [5, 8], [6, 9]], 7) == 2)
    test(count_overlapping([[1, 2], [2, 3], [3, 4]], 5) == 0)
    test(count_overlapping([[1, 2], [5, 6], [5, 7]], 5) == 2)
    test(count_overlapping([[1, 2], [5, 8], [6, 9]], 7) == 2)
    test(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5) == 5)
    test(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 6) == 2)
    test(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 2) == 2)
    test(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1) == 1)
    test(in_box([
        "###",
        "#*#",
        "###"
    ]))

    test(in_box([
        "####",
        "#* #",
        "#  #",
        "####"
    ]))

    test(not in_box([
        "####",
        "#  #",
        "#  #",
        "####"
    ]))

    test(not in_box([
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ]))


if __name__ == '__main__':
    test_suite()
