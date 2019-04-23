from under100.day65 import test
import string


# https://edabit.com/challenge/FSRLWWcvPRRdnuDpv
def time_to_eat(a_str):
    exclude = set(string.punctuation)
    a_str = ''.join(ch for ch in a_str if ch not in exclude)
    time_minutes = convert_minutes(a_str)
    print(time_minutes)
    if 420 < time_minutes < 720:
        a_list = minutes_d(time_minutes, 0)
        print(a_list)
        return [a_list[0], a_list[1]]
    if time_minutes == 720:
        return [7, 0]
    if time_minutes == 420:
        return [12, 0]
    if time_minutes < 420:
        return minutes_d(time_minutes, 420)


def minutes_d(time_minutes, d):
    num_minutes = d - time_minutes
    hours = int(num_minutes / 60)
    minutes = num_minutes % 60
    return [abs(hours), minutes]


def convert_minutes(a_str):
    the_time = a_str.split()
    time_12 = the_time[0]
    hours = int(time_12[:-2])
    minutes = int(time_12[-2:])
    time_minutes = (hours * 60) + minutes
    return time_minutes


def test_suite():
    test(time_to_eat("2:00 p.m.") == [5, 0])
    test(time_to_eat("5:50 a.m.") == [1, 10])
    test((time_to_eat("6:37 p.m.") == [0, 23]))
    test((time_to_eat("12:00 a.m.") == [7, 0]))
    test((time_to_eat("11:58 p.m.") == [7, 2]))
    test((time_to_eat("3:33 p.m.") == [3, 27]))


if __name__ == '__main__':
    test_suite()
