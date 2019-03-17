from under100.day65 import test


# def lone_sum(a, b, c):
#     sum = 0
#     if a != b and a != c: sum += a
#     if b != a and b != c: sum += b
#     if c != a and c != b: sum += c
#
#     return sum
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    a, b = lone_sum_helper(a, b)
    a, c = lone_sum_helper(a, c)
    b, c = lone_sum_helper(b, c)
    return sum([a, b, c])


def lone_sum_helper(n1, n2):
    if n1 == n2:
        return 0, 0
    return n1, n2


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if (num % 10) < 5:
        return num - num % 10
    return num + (10 - num % 10)


def lucky_sum(a, b, c):
    sum = 0
    if a == 13:
        return sum
    sum += a
    if b == 13:
        return sum
    sum += b
    if c == 13:
        return sum
    sum += c
    return sum


def close_far(a, b, c):
    if abs(a - b) <= 1 < abs(a - c) and abs(b - c) > 1:
        return True
    if abs(a - c) <= 1 < abs(a - b) and abs(b - c) > 1:
        return True
    return False


def test_suite():
    test(lone_sum(1, 2, 3) == 6)
    test(lone_sum(3, 2, 3) == 2)
    test(lone_sum(3, 3, 3) == 0)
    test(round_sum(16, 17, 18) == 60)
    test(round_sum(12, 13, 14) == 30)
    test(round_sum(6, 4, 4) == 10)
    test(lucky_sum(1, 2, 3) == 6)
    test(lucky_sum(1, 2, 13) == 3)
    test(lucky_sum(1, 13, 3) == 1)
    test(close_far(1, 2, 10))
    test(not close_far(1, 2, 3))
    test(close_far(4, 1, 3))


if __name__ == '__main__':
    test_suite()
