from under100.day65 import test


# https://edabit.com/challenge/AjZBGWyPaA7rXFhi6
def min_swaps(str1, str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            counter += 1
    return counter / 2


def test_suite():
    test(min_swaps("1100", "1001") == 1)
    test(min_swaps("110011", "010111") == 1)
    test(min_swaps("10011001", "01100110") == 4)
    test(min_swaps("1001", "1001") == 0)
    test(min_swaps("1100", "1001") == 1)
    test(min_swaps("110011", "010111") == 1)
    test(min_swaps("1100", "0011") == 2)
    test(min_swaps("110011", "001111") == 2)
    test(min_swaps("10011001", "01100101") == 3)
    test(min_swaps("11111000001100", "10110010100110") == 3)
    test(min_swaps("01100100100111", "10110010100110") == 3)
    test(min_swaps("11110011001", "01100110111") == 3)
    test(min_swaps("100110001", "010100110") == 3)
    test(min_swaps("100101011", "011001101") == 3)
    test(min_swaps("10011001", "01100110") == 4)


if __name__ == '__main__':
    test_suite()
