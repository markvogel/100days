import random


# https://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html

def default_app():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(set(a).intersection(b))

    # this works, but doesn't feel right
    c = [x for x in a and b if x in a and x in b]

    print(c)


def extra_app():
    r1 = [random.randint(0, 10) for i in range(10)]
    r2 = [random.randint(0, 10) for i in range(10)]
    return [i for i in r1 if i in r2]


def get_number():
    return input('Please enter a number: ')


def create_list(num1):
    return range(1, int(num1) + 1)


def calc_divisors(number: int):
    return [i for i in create_list(number) if number % i == 0]


# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def check_prime(num: int):
    if len(calc_divisors(num)) <= 2:
        print("You entered a prime number!")
    else:
        print("The number that you entered is not a prime.")


if __name__ == '__main__':
    # print(extra_app())
    # default_app()
    n = get_number()
    check_prime(int(n))
