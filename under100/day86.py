from under100.day65 import test


def percent_diff(num1, num2):
    diff = abs((num1 - num2) / ((num1 + num2) / 2)) * 100
    return round(diff, ndigits=1)


def overlap(str1, str2):
    a, b = str1.lower(), str2.lower()
    c, d = min(a, b), max(a, b)
    print(c, d)
    if ("*" * len(c)) == d[-len(c):]:
        return True
    if c == d[-len(c):]:
        return True
    return False


def test_suite():
    test(first_last([5, 10, 15, 20, 25]) == [5, 25])
    test(first_last(["edabit", 13, None, False, True]) == ["edabit", True])
    test(first_last([None, 4, "6", "hello", None]) == [None, None])
    test(percent_diff(60, 100) == 50.0)
    test(percent_diff(100, 60) == 50.0)
    test(percent_diff(4538, 5439) == 18.1)
    test(percent_diff(4538, 5439) == 18.1)
    test(overlap("ABC", "Ican'tsingmyABC"))
    test(overlap("abc", "Ican'tsingmyABC"))
    test(overlap("Ican'tsingmyABC", "abc"))
    test(not overlap("hello world", "hello"))
    test(overlap("+=", "this should work too +="))
    test(overlap("hey", "*********"))  # not handling this properly


def first_last(a_list):
    return [a_list[0], a_list[-1]]


if __name__ == '__main__':
    test_suite()
