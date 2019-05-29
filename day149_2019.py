from under100.day65 import test


# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
def char_input():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    copies = int(input("How many times would you like me to print?"))
    print(f"{name}, you will turn 100 in {100 - age} years\n" * copies)

    # for i in range(copies):
    #     print(f"{name}, you will turn 100 in {100 - age} years")


def test_suite():
    pass


# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
def odd_even():
    num = int(input("Please enter a number: "))
    if num % 2:
        print(f"{num} is an odd number")
    elif not num % 4:
        print(f"{num} is a multiple of four")
    elif not num % 2:
        print(f"{num} is an even number")


def num_check():
    num = int(input("Please enter a number: "))
    check = int(input("Please enter a number to divide by: "))
    if not num % check:
        print(f"{check} divides evenly into {num}")
    else:
        print(f"{check} doesn't divide evenly into {num}")


if __name__ == '__main__':
    # test_suite()
    # char_input()
    # odd_even()
    num_check()
