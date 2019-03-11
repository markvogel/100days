from day65 import test
import numpy as np


def test_suite():
    test(not change_enough([2, 100, 0, 0], 14.11))
    test(change_enough([0, 0, 20, 5], 0.75))
    test(change_enough([30, 40, 20, 5], 12.55))
    test(not change_enough([10, 0, 0, 50], 3.85))
    test(not change_enough([1, 0, 5, 219], 19.99))
    test(not change_enough([2, 100, 0, 0], 14.11))
    test(change_enough([0, 0, 20, 5], 0.75))
    test(change_enough([30, 40, 20, 5], 12.55))
    test(not change_enough([10, 0, 0, 50], 13.85))
    test(not change_enough([1, 0, 5, 219], 19.99))
    test(change_enough([1, 0, 2555, 219], 127.75))
    test(change_enough([1, 335, 0, 219], 35.21))


"""Given a total due and a list representing the amount of change in your pocket, determine whether or not you are able
 to pay for the item. Change will always be represented in the following order: quarters, dimes, nickels, pennies.
To illustrate: change_enough([25, 20, 5, 0], 4.25) should yield True, since having 25 quarters, 20 dimes, 5 nickels and
 1 penny gives you 6.25 + 2 + .25 + 0 = 8.50."""


# https://edabit.com/challenge/phMpXM9nu52bCjguS
def change_enough(change, amount_due):
    c = np.array(change)
    change_conversion_list = np.array([.25, .10, .05, .01])
    change_list = c * change_conversion_list
    if sum(change_list) >= amount_due:
        return True
    return False


if __name__ == '__main__':
    test_suite()
