from under100.day65 import test


# https://edabit.com/challenge/y5WQ54rzwEg3iga9f
def profit(a, b):
    a_profit = 0
    b_profit = 0

    for i in range(100):
        if abs(i - a) < abs(i - b):
            a_profit += 1
        if abs(i - a) >= abs(i - b):
            b_profit += 1
    print(a_profit, b_profit)
    return [a_profit, b_profit]


def test_suite():
    test(profit(32, 69) == [51, 50])
    test(profit(49, 51) == [50, 50])
    test(profit(25, 26) == [26, 75])
    test(profit(24, 26) == [25, 75])
    test(profit(0, 1) == [1, 100])
    test(profit(3, 6) == [5, 96])
    test(profit(55, 65) == [60, 40])
    test(profit(25, 75) == [50, 50])


if __name__ == '__main__':
    test_suite()
