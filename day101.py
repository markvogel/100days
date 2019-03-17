from under100.day65 import test


# https://edabit.com/challenge/G5FXsvc8hD6DqnCKx
def convert_time(time_str):
    return hours(time_str)


def hours(a_str):
    hour = 0
    if len(a_str) <= 5:
        int_hours = int(a_str.split(sep=":")[0])
        if int_hours == 12:
            return str(int_hours) + ":" + a_str.split(sep=":")[1] + " pm"
        if int_hours > 12:
            return str(int_hours - 12) + ":" + a_str.split(sep=":")[1] + " pm"
        if int_hours < 12:
            return str(int_hours) + ":" + a_str.split(sep=":")[1] + " am"
    int_hours = int(a_str.split()[0][:-3])
    if a_str.endswith("am"):
        hour = int_hours - 12
    if a_str.endswith("pm"):
        hour = int_hours + 12
    return str(hour) + a_str.split()[0][-3:]


def test_suite():
    test(convert_time("12:00 am") == "0:00")
    test(convert_time("6:20 pm") == "18:20")
    test(convert_time("21:00") == "9:00 pm")
    test(convert_time("5:05") == "5:05 am")


if __name__ == '__main__':
    test_suite()
