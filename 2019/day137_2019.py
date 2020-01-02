from under100.day65 import test


def box():
    c = 0
    while c < 4:
        print("*" * 20)
        c += 1


def open_box():
    print("*" * 20)
    print("*" + " " * 18 + "*")
    print("*" + " " * 18 + "*")
    print("*" * 20)


def triangle():
    for i in range(1, 5):
        print("*" * i)


def foo():
    print((512 - 282) / ((47 * 48) + 5))


def print_square():
    a = input("Enter a number: ")
    print(f"The square of {a} is {int(a) ** 2}", end=".")


def test_suite():
    pass


if __name__ == '__main__':
    test_suite()
    # box()
    # open_box()
    # triangle()
    # foo()
    print_square()
