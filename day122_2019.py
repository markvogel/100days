from under100.day65 import test


def can_complete(str1, str2):
    for i in range(len(str1)):
        if str1[i] not in str2:
            return False
        # if str1[i] == str2[i]:
        #     continue
    return True


def test_suite():
    test(can_complete('butl', 'beautiful'))
    test(not can_complete('butlz', 'beautiful'))
    test(not can_complete('tulb', 'beautiful'))
    test(not can_complete('bbutl', 'beautiful'))
    test(can_complete('sg', 'something'))
    test(not can_complete('sgi', 'something'))
    test(can_complete('sing', 'something'))
    test(not can_complete('siing', 'something'))


if __name__ == '__main__':
    test_suite()
