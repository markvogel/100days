from under100.day65 import test


# TODO doesn't work, need to fix
# https://edabit.com/challenge/ZFLmA6Xjt8gNxg4KR
def sum_consecutives(a_list):
    new_list = []
    for i in range(len(a_list)):
        for ii in a_list:
            if not ii % i:
                if a_list[i] == a_list[i + 1]:
            new_list.append(a_list[i] + a_list[i + 1])
            continue
        new_list.append(int(a_list[i]))
    return new_list


# https://edabit.com/challenge/GaXXfmpM72yCHag9T
def unique(a_list):
    for i in a_list:
        if a_list.count(i) == 1:
            return i


def test_suite():
    test(sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]) == [0, 21, 5, 4, 18, 0])
    test(sum_consecutives([4, 4, 5, 6, 8, 8, 8]) == [8, 5, 6, 24])
    test(sum_consecutives([-5, -5, 7, 7, 12, 0]) == [-10, 14, 12, 0])
    test(unique([3, 3, 3, 7, 3, 3]) == 7)
    test(unique([0, 0, 0.77, 0, 0]) == 0.77)
    test(unique([0, 1, 1, 1, 1, 1, 1, 1]) == 0)


if __name__ == '__main__':
    test_suite()
