from under100.day65 import test


# https://edabit.com/challenge/eDQDChGrv6y4fd44j
# TODO test on line 27 fails
def can_put(txt, dim):
    if len(txt) <= dim[1]:
        return True
    lst = txt.split()
    for i in range(len(lst)):
        if len(lst[i]) <= dim[1] and i <= dim[0]:
            continue
        else:
            return False
    if len(txt.replace(" ", "")) == dim[1]:
        return False
    return True


def test_suite():
    test(can_put("HEY JUDE", [2, 4]))
    test(can_put("HEY JUDE", [1, 8]))
    test(not can_put("HEY JUDE", [1, 7]))  # 'cannot fit leaving a space in')
    test(not can_put("HEY JUDE", [4, 3]))  # 'JUDE cannot fit on second row')
    test(not can_put("CU L8R", [2, 2]))  # 'L8R cannot fit on second row')
    test(not can_put("CU L8R", [1, 5]))  # 'cannot fit leaving a space in')
    test(can_put("CU L8R", [5, 5]))
    test(can_put("BEAUTY IS WITHIN", [3, 6]))
    test(not can_put("BEAUTY IS WITHIN", [4, 5]))


if __name__ == '__main__':
    test_suite()
