from under100.day65 import test


# https://bids.github.io/2016-01-14-berkeley/python/00-python-intro.html
def convert_inches_meters(inches):
    inches_in_meter = 39.3701
    metres = inches / inches_in_meter
    print(round(metres, ndigits=2))


def convert_feet_meters(feet, inches):
    inches_in_meter = 39.3701
    meters = ((feet * 12) + inches) / inches_in_meter
    print(round(meters, ndigits=2))


def foo():
    heights = [1.5, 1.78, 1.23, 1.99, 1.57, 1.88]
    print(heights[0], heights[len(heights) - 1], heights[-1])


def test_suite():
    pass


if __name__ == '__main__':
    test_suite()
    # convert_inches_meters(40)
    # convert_feet_meters(6, 2)
    foo()
