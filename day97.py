from day65 import test


# https://edabit.com/challenge/34oMwAoamvw7HyYGu
# TODO not working, great practice problem
def combinator(lst):
    new_lst = []
    if not len(lst):
        return lst[0]
    for i in range(len(lst)):
        for ii in range(len(lst[i])):
            new_lst.append(lst[i][ii])
    for i in range(len(new_lst)):
        new_lst[i] += "a"
    print(new_lst)
    # for i in range(len(lst)):


def join_2(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] + lst2[i])
    return result


def test_suite():
    test(combinator([["a", "b"], ["c", "d"]]) == ["ac", "ad", "bc", "bd"])
    test(combinator([["foo", "bar"], ["baz", "bamboo"]]) == ["foo baz", "foo bamboo", "bar baz", "bar bamboo"])
    test(combinator([[]]) == [])


if __name__ == '__main__':
    test_suite()
    print(join_2(["a", "b"], ["c", "d"]))
    # print(combinator([["a", "b"], ["c", "d"]]))
