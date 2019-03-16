import psutil
from day65 import test


def steps_to_convert(a_string):
    if not len(a_string):
        return 0
    if a_string.islower() or a_string.isupper():
        return 0
    count = 0
    for i in range(len(a_string)):
        if a_string[i].islower():
            count += 1
    a = [count, len(a_string) - count]
    return min(a)


def equal_slices(total, people, each):
    return (total / people) >= each


def test_suite():
    test(steps_to_convert("abC") == 1)
    test(steps_to_convert("abCBA") == 2)
    test(steps_to_convert("aba") == 0)
    test(steps_to_convert("abaCCC") == 3)
    test(steps_to_convert('abC') == 1)
    test(steps_to_convert('abCBA') == 2)
    test(steps_to_convert('aba') == 0)
    test(steps_to_convert('ABA') == 0)
    test(steps_to_convert('abaCCC') == 3)
    test(steps_to_convert('abaaCCCDE') == 4)
    test(steps_to_convert('CCaaCCaaCa') == 5)
    test(steps_to_convert('') == 0)
    test(equal_slices(11, 5, 2))
    test(not equal_slices(11, 5, 3))
    test(equal_slices(8, 3, 2))
    test(not equal_slices(8, 3, 3))
    test(equal_slices(24, 12, 2))


def battery_info():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if not plugged:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
    print(percent + '% | ' + plugged)


if __name__ == '__main__':
    # battery_info()
    test_suite()
