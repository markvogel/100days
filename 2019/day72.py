# https://codingbat.com/python/Logic-1

from under100.day65 import test


def cigar_party(cigars, is_weekend):
    if is_weekend:
        return 39 < cigars
    return 39 < cigars < 61


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed < 61:
        return 0
    if 60 < speed < 81:
        return 1
    if speed > 80:
        return 2


def love6(a, b):
    return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1


def sorta_sum(a, b):
    sum = a + b
    if 10 <= sum <= 19:
        return 20
    return sum


def in1to10(n, outside_mode):
    if outside_mode:
        if n not in range(2, 10):
            return True
        return False
    return n in range(1, 11)


def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90


def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        return "10:00"
    if day == 0 or day == 6:
        return "10:00"
    return "7:00"


def near_ten(num):
    close = (num % 10)
    if close <= 2 or close >= 8:
        return True
    return False


def test_suite():
    test(not cigar_party(30, False))
    test(cigar_party(50, False))
    test(cigar_party(70, True))
    test(caught_speeding(60, False) == 0)
    test(caught_speeding(65, False) == 1)
    test(caught_speeding(65, True) == 0)
    test(love6(6, 4))
    test(not love6(4, 5))
    test(love6(1, 5))
    test(date_fashion(5, 10) == 2)
    test(date_fashion(5, 2) == 0)
    test(date_fashion(5, 5) == 1)
    test(sorta_sum(3, 4) == 7)
    test(sorta_sum(9, 4) == 20)
    test(sorta_sum(10, 11) == 21)
    test(in1to10(5, False))
    test(not in1to10(11, False))
    test(in1to10(11, True))
    test(squirrel_play(70, False))
    test(not squirrel_play(95, False))
    test(squirrel_play(95, True))
    test(alarm_clock(1, False) == '7:00')
    test(alarm_clock(5, False) == '7:00')
    test(alarm_clock(0, False) == '10:00')
    test(near_ten(12))
    test(not near_ten(17))
    test(near_ten(19))


if __name__ == '__main__':
    test_suite()
