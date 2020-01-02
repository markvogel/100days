from under100.day65 import test


# https://edabit.com/challenge/XsqET8hSTBG2AR5kM
def letter_distance(str1, str2):
    letter_list = [dist(str1[i], str2[i]) for i in range(len(str1))]
    letter_list.append(abs(len(str1) - len(str2)))
    return sum(letter_list)


def dist(a, b):
    return abs(ord(a) - ord(b))


# https://edabit.com/challenge/Egh2HES8eqPTTX9Q2
def rolling_cipher(a_str, n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_dict = {letters[i]: i for i in range(len(letters))}
    letter_list = [letter_dict.get(a_str[i]) for i in range(len(a_str))]
    new_letter_list = [alpha_num(i + n) for i in letter_list]
    new_letter_list2 = [list(letter_dict.keys())[i] for i in new_letter_list]
    return ''.join(new_letter_list2)


def alpha_num(a):
    if 0 <= a <= 25:
        return a
    if a > 25:
        return a - 26
    if a < 25:
        return a + 26


def test_suite():
    test(letter_distance("sharp", "sharq") == 1)
    test(letter_distance("abcde", "Abcde") == 32)
    test(letter_distance("abcde", "bcdef") == 5)
    test(rolling_cipher("abcd", 1) == "bcde")
    test(rolling_cipher("abcd", -1) == "zabc")
    test(rolling_cipher("abcd", 3) == "defg")
    test(rolling_cipher("abcd", 26) == "abcd")


if __name__ == '__main__':
    test_suite()
