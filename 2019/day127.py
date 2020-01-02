from under100.day65 import test


# https://edabit.com/challenge/zqMREZ2MQd9M5jNfM
def is_symmetrical(a_num):
    a_str = str(a_num)
    return a_str == a_str[::-1]


# https://edabit.com/challenge/9TcXrWEGH3DaCgPBs
def find_odd(a_list):
    for i in a_list:
        if a_list.count(i) % 2:
            return i


def test_suite():
    test(is_symmetrical(7227))
    test(not is_symmetrical(12567))
    test(is_symmetrical(44444444))
    test(not is_symmetrical(9939))
    test(is_symmetrical(1112111))
    test(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1)
    test(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5)
    test(find_odd([10]) == 10)


if __name__ == '__main__':
    test_suite()
