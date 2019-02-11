# https://codingbat.com/prob/p149524
from day65 import test


def missing_char(s: str, n: int):
    return s[:n] + s[n + 1:]


def pos_neg(a, b, negative):
    if not negative:
        if a > 0 > b or b > 0 > a:
            return True
    if a < 0 and b < 0 and negative:
        return True
    return False


def test_suite():
    test(missing_char('kitten', 1) == 'ktten')
    test(missing_char('kitten', 0) == 'itten')
    test(missing_char('kitten', 4) == 'kittn')
    test(pos_neg(1, -1, False))
    test(pos_neg(-1, 1, False))
    test(pos_neg(-4, -5, True))


if __name__ == '__main__':
    test_suite()
