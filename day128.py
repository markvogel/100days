from under100.day65 import test


def is_valid_PIN(pin):
    if not pin.isdigit():
        return False
    a = len(pin)
    if a == 4 or a == 6:
        return True
    return False


def test_suite():
    test(is_valid_PIN("1234"))
    test(not is_valid_PIN("12345"))
    test(not is_valid_PIN("a234"))
    test(not is_valid_PIN(""))


if __name__ == '__main__':
    test_suite()
