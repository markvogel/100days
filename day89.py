from day65 import test


def find_frequent(lst):
    if not len(lst):
        return None
    count = 0
    var = ''
    set_lst = set(lst)
    for i in set_lst:
        if lst.count(i) >= count:
            count = lst.count(i)
            var = i
    return var


def expand(a_num):
    a_num = str(a_num)
    num_list = []
    for i, v in enumerate(a_num):
        if v == '0':
            break
        num_list.append(v + "0" * (len(a_num) - i - 1))
    return " + ".join(num_list)


def test_suite():
    test(find_frequent([3, 7, 3]) == 3)
    test(find_frequent([None, "hello", True, None]) is None)
    test(not find_frequent([False, "up", "down", "left", "right", True, False]))
    test(expand(13) == "10 + 3")
    test(expand(86) == "80 + 6")
    test(expand(17000000) == "10000000 + 7000000")
    test(expand(5325) == "5000 + 300 + 20 + 5")


if __name__ == '__main__':
    test_suite()
