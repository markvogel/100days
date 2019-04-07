from under100.day65 import test


# https://edabit.com/challenge/E8TSTy4R5eWEkkaKf
def is_valid(txt):
    txt_lst = txt.split(sep=".")
    if len(txt_lst) > 4 or len(txt_lst) < 4:
        return False
    for i in txt_lst:
        if 0 <= int(i) <= 255:
            continue
        else:
            return False
    return True


def test_suite():
    test(is_valid("1.2.3.4"))
    test(not is_valid("1.2.3"))
    test(not is_valid("1.2.3.4.5"))
    test(is_valid("123.45.67.89"))
    test(not is_valid("123.456.78.90"))
    test(is_valid("123.045.067.089"))


if __name__ == '__main__':
    test_suite()
