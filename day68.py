# https://codingbat.com/prob/p189441

from day65 import test


def not_string(param: str):
    if not param.startswith('not'):
        return "not " + param
    return param


def front3(param1):
    front = param1[:3]
    # if len(param1) < 3:
    #     front = param1
    return front * 3


def front3_2(param1):
    return param1[:3] * 3


def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def makes10(a, b):
    return a == 10 or 10 == b or a + b == 10


def sum_double(a, b):
    sum = a + b
    if a == b:
        sum *= 2
    return sum


def front_back(param):
    if len(param) <= 1:
        return param
    return param[-1] + param[1:len(param) - 1] + param[0]


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 < b) or (a > 0 > b)


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False


def missing_char(s, n):
    return s[:n] + s[n + 1:]


def diff21(n):
    d = abs(21 - n)
    if n > 21:
        d *= 2
    return d


def sleep_in(weekday, vacation):
    return not weekday or vacation


def test_suite():
    test(sleep_in(False, False))
    test(not sleep_in(True, False))
    test(sleep_in(False, True))
    test(diff21(19) == 2)
    test(diff21(10) == 11)
    test(diff21(21) == 0)
    test(near_hundred(93))
    test(near_hundred(90))
    test(not near_hundred(89))
    test(missing_char('kitten', 1) == 'ktten')
    test(missing_char('kitten', 0) == 'itten')
    test(missing_char('kitten', 4) == 'kittn')
    test(monkey_trouble(True, True))
    test(monkey_trouble(False, False))
    test(not monkey_trouble(True, False))
    test(parrot_trouble(True, 6))
    test(not parrot_trouble(True, 7))
    test(not parrot_trouble(False, 6))
    test(pos_neg(1, -1, False))
    test(pos_neg(-1, 1, False))
    test(pos_neg(-4, -5, True))
    test(front_back('code') == 'eodc')
    test(front_back('a') == 'a')
    test(front_back('ab') == 'ba')
    test(sum_double(1, 2) == 3)
    test(sum_double(3, 2) == 5)
    test(sum_double(2, 2) == 8)
    test(makes10(9, 10))
    test(not makes10(9, 9))
    test(makes10(1, 9))
    test(not_string('candy') == 'not candy')
    test(not_string('x') == 'not x')
    test(not_string('not bad') == 'not bad')
    test(front3('Java') == 'JavJavJav')
    test(front3('Chocolate') == 'ChoChoCho')
    test(front3('abc') == 'abcabcabc')
    test(front3_2('Java') == 'JavJavJav')
    test(front3_2('Chocolate') == 'ChoChoCho')
    test(front3_2('abc') == 'abcabcabc')


if __name__ == '__main__':
    test_suite()
