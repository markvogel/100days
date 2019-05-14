from under100.day65 import test


# https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/
def max2(n1, n2):
    if n1 >= n2:
        return n1
    return n2


def fizz_buzz(n):
    if not n % 3 and not n % 5:
        return "FizzBuzz"
    if not n % 3:
        return "Fizz"
    if not n % 5:
        return "Buzz"
    return n


def check_speed(speed):
    if speed < 70:
        print("Ok")
    d = int((speed - 70) / 5)
    if d > 12:
        print("License suspended")


def test_suite():
    test(max2(1, 2) == 2)
    test(max2(100, 2) == 100)
    test(max2(44, 44) == 44)
    test(fizz_buzz(15) == "FizzBuzz")
    test(fizz_buzz(33) == "Fizz")
    test(fizz_buzz(10) == "Buzz")
    test(fizz_buzz(101) == 101)
    check_speed(140)
    check_speed(69)
    check_speed(1)


if __name__ == '__main__':
    test_suite()
