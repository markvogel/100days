from under100.day65 import test


# https://edabit.com/challenge/K4Pqh67Y9gpixPfjo
def is_valid_PIN(pin):
    if not pin.isdigit():
        return False
    a = len(pin)
    return a == 4 or a == 6


def test_suite():
    test(is_valid_PIN("1234"))
    test(not is_valid_PIN("12345"))
    test(not is_valid_PIN("a234"))
    test(not is_valid_PIN(""))


if __name__ == '__main__':
    test_suite()
