from under100.day65 import test


def is_in_range(num, a_dict):
    return a_dict.get("min") <= num <= a_dict.get("max")


def has_spaces(a_str):
    return a_str.__contains__(" ")


def countdown(num):
    return [abs(num - i) for i in range(num + 1)]


def test_suite():
    test(is_in_range(4, {"min": 0, "max": 5}))
    test(is_in_range(4, {"min": 4, "max": 5}))
    test(is_in_range(4, {"min": 0, "max": 4}))
    test(not is_in_range(4, {"min": 6, "max": 10}))
    test(not is_in_range(11, {"min": 6, "max": 10}))
    test(is_in_range(5, {"min": 5, "max": 5}))
    test(is_in_range(1.5, {"min": 1.25, "max": 1.75}))
    test(not is_in_range(1.1, {"min": 1.25, "max": 1.75}))
    test(not is_in_range(1.8, {"min": 1.25, "max": 1.75}))
    test(is_in_range(-1, {"min": -1, "max": 1}))
    test(not has_spaces("Foo"))
    test(has_spaces("Foo bar"))
    test(has_spaces("Foo "))
    test(has_spaces(" Foo"))
    test(has_spaces(" "))
    test(not has_spaces(""))
    test(not has_spaces(",./;'[]-="))
    test((countdown(3) == [3, 2, 1, 0]))
    test((countdown(20) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
    test((countdown(1) == [1, 0]))
    test((countdown(0) == [0]))


if __name__ == '__main__':
    test_suite()
