from under100.day65 import test


def make_bricks(small, big, goal):
    if goal > big * 5 + small:
        return False
    return not goal % 5 > small


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n in range(13, 20):
        if n == 15 or n == 16:
            return n
        return 0
    return n


# def make_chocolate(small, big, goal):
#   if goal > big * 5 + small:
#     return -1
#   if goal % 5 > small:
#     return -1
#   return (goal - big * 5)

def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
    if remainder <= small:
        return remainder
    return -1


def test_suite():
    test(make_bricks(3, 1, 8))
    test(not make_bricks(3, 1, 9))
    test(make_bricks(3, 2, 10))
    test(no_teen_sum(1, 2, 3) == 6)
    test(no_teen_sum(2, 13, 1) == 3)
    test(no_teen_sum(2, 1, 14) == 3)
    test(make_chocolate(4, 1, 9) == 4)
    test(make_chocolate(4, 1, 10) == -1)
    test(make_chocolate(4, 1, 7) == 2)


if __name__ == '__main__':
    test_suite()
