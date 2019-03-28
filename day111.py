from under100.day65 import test


# https://edabit.com/challenge/YzcnFjMEKQfyHAg6B
def simon_says(num_list1, num_list2):
    for i in range(len(num_list2) - 1):
        if num_list2[i + 1] != num_list1[i]:
            return False
    return True


def test_suite():
    test(simon_says(
        [1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4]
    ))

    test(not simon_says(
        [1, 2, 3, 4, 5],
        [5, 5, 1, 2, 3]))

    test(simon_says(
        [1, 2],
        [5, 1]
    ))

    test(not simon_says(
        [1, 2],
        [5, 5]
    ))

    test(simon_says(
        [1, 2, 3],
        [0, 1, 2]
    ))


if __name__ == '__main__':
    test_suite()
