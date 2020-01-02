from under100.day65 import test


def convert_2fahrenheit(c_temp):
    return (9 / 5) * c_temp + 32


def convert_2celsius(f_temp):
    return (5 / 9) * (f_temp - 32)


# http://openbookproject.net/pybiblio/practice/wilson/tempfinder.php
def get_temperature():
    temp = input("Enter a temperature: ")
    temp = int(temp)
    conv = ""
    while conv.lower() != "f" and conv.lower() != "c":
        conv = input("Convert to (F)ahrenheit or (C)elsius? ")
    if conv.lower() == "f":
        print(f"{temp} C = {int(convert_2fahrenheit(temp))} F")
        return
    print(f"{temp} F = {int(convert_2celsius(temp))} C")
    return


def test_suite():
    test(convert_2fahrenheit(0) == 32)
    test(convert_2celsius(32) == 0)


if __name__ == '__main__':
    test_suite()
    get_temperature()
