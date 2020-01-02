from under100.day65 import test


# https://edabit.com/challenge/WQjynmyMXcR83Dd8K
def number_of_swaps(num_list):
    counter = 0
    while num_list != sorted(num_list):
        for i in range(1, len(num_list)):
            if num_list[i] < num_list[i - 1]:
                num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
                counter += 1
    return counter


# TODO does not work (IndexError: list index out of range)
# https://edabit.com/challenge/v3iQ4XiW385SrkWKo
def final_result(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i:i + 2].count(a_list[i]) == 2:
            del a_list[i:i + 2]

        print(a_list)


def test_suite():
    # test(number_of_swaps([5, 4, 3]) == 3)
    # test(number_of_swaps([1, 3, 4, 5]) == 0)
    # test(number_of_swaps([5, 4, 3, 2]) == 6)
    # test((number_of_swaps([3, 9, 7, 4]) == 3))
    # test((number_of_swaps([5, 4, 3]) == 3))
    # test((number_of_swaps([5, 4, 3, 2]) == 6))
    # test((number_of_swaps([1, 2, 4, 3]) == 1))
    # test((number_of_swaps([1, 2, 5, 4, 3]) == 3))
    # test((number_of_swaps([1, 3, 4, 5]) == 0))
    # test((number_of_swaps([1, 2]) == 0))
    test(final_result(["B", "B", "A", "C", "A", "A", "C"]) == ["A"])
    test(final_result(["B", "B", "C", "C", "A", "A", "A"]) == [])
    test(final_result(["C", "A", "C"]) == ["C", "A", "C"])


if __name__ == '__main__':
    test_suite()
