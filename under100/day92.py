from under100.day65 import test


def count_words(param):
    return len([i for i in param.split()])


def missing_letter(a_list):
    char_ints = [ord(i) for i in a_list]
    start = char_ints[0]
    for ii in range(start, start + len(char_ints)):
        if char_ints[ii - start] != char_ints[(ii - start) + 1]:
            print(chr(ii + 1))
            return chr(ii + 1)


def test_suite():
    test(count_words("Just an example here move along") == 6)
    test(count_words("This is a test") == 4)
    test(count_words("What an easy task, right") == 5)
    test(missing_letter(["a", "b", "c", "e", "f", "g"]) == "d")
    test(missing_letter(["O", "Q", "R", "S"]) == "P")
    test(missing_letter(["t", "u", "v", "w", "x", "z"]) == "y")
    test(missing_letter(["m", "o"]) == "n")


if __name__ == '__main__':
    test_suite()
