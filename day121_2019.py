from under100.day65 import test


# https://edabit.com/challenge/FeNrBCG9rSdNeJTuX
def max_possible(num1, num2):
    list1, list2 = make_list_from_num(num1), make_list_from_num(num2)
    maximum = ""
    for i in range(len(list1)):
        if not len(list2):
            b = [str(i) for i in list1[len(maximum):]]
            "".join(b)
            maximum += "".join(b)
            break
        if max(list2) > list1[i]:
            maximum += str(max(list2))
            list2.remove(max(list2))
        else:
            maximum += str(list1[i])
    return int(maximum)


def make_list_from_num(a):
    return [int(i) for i in str(a)]


def test_suite():
    test(make_list_from_num(121) == [1, 2, 1])
    test(max_possible(9328, 456) == 9658)
    test(max_possible(523, 76) == 763)
    test(max_possible(9132, 5564) == 9655)
    test(max_possible(8732, 91255) == 9755)
    test(max_possible(589, 777) == 789)
    test(max_possible(1, 0) == 1)
    test(max_possible(8, 9) == 9)
    test(max_possible(28, 19) == 98)
    test(max_possible(12345, 4) == 42345)


if __name__ == '__main__':
    test_suite()
