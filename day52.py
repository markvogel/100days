# http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html
# 6.9. Exercises 1-5

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    # test(absolute_value(17) == 17)
    # test(absolute_value(-17) == 17)
    # test(absolute_value(0) == 0)
    # test(absolute_value(3.14) == 3.14)
    # test(absolute_value(-3.14) == 3.14)
    # test(turn_clockwise("N") == "E")
    # test(turn_clockwise("W") == "N")
    # test(turn_clockwise(42) is None)
    # test(turn_clockwise("rubbish") is None)
    # test(day_name(3) == "Wednesday")
    # test(day_name(6) == "Saturday")
    # test(day_name(42) is None)
    # test(day_num("Friday") == 5)
    # test(day_num("Sunday") == 0)
    # test(day_num(day_name(3)) == 3)
    # test(day_name(day_num("Thursday")) == "Thursday")
    # test(day_num("Halloween") is None)
    # test(day_add("Monday", 4) == "Friday")
    # test(day_add("Tuesday", 0) == "Tuesday")
    # test(day_add("Tuesday", 14) == "Tuesday")
    # test(day_add("Sunday", 100) == "Tuesday")
    # test(day_add("Sunday", -1) == "Saturday")
    # test(day_add("Sunday", -7) == "Sunday")
    # test(day_add("Tuesday", -100) == "Sunday")
    # test(days_in_month("February") == 28)
    # test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)


def absolute_value(x):
    if x < 0:
        return -x
    return x


def turn_clockwise(a: str):
    turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    return turn.get(a)


def day_name(b: int):
    day_names = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return day_names.get(b)


def day_num(d: str):
    day_names = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    for num, day in day_names.items():
        if day == d:
            return num


def day_add(day: str, days_to_add: int):
    x = day_num(day) + days_to_add
    x = x % 7
    return day_name(x)


def day_name2(c: int):
    day = None
    if c == 0:
        day = 'Sunday'
    if c == 1:
        day = 'Monday'
    if c == 2:
        day = 'Tuesday'
    if c == 3:
        day = 'Wednesday'
    if c == 4:
        day = 'Thursday'
    if c == 5:
        day = 'Friday'
    if c == 6:
        day = 'Saturday'
    return day


# number 6 - http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html
def days_in_month(month_name: str):
    month_abbrev = month_name[:3].lower()
    total_days = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30,
                  'oct': 31, 'nov': 30, 'dec': 31}
    return total_days.get(month_abbrev)


def to_secs(hours_in, minutes_in, seconds_in):
    total_seconds = (hours_in * 3600) + (minutes_in * 60) + seconds_in
    return int(total_seconds)


if __name__ == '__main__':
    test_suite()  # Here is the call to run the tests
