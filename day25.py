# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# get a number from the user and calculate all divisors of that number


def get_number():
    return input('Please enter a number: ')


def create_list(num1):
    return range(1, int(num1) + 1)


def calc_divisor(num2):
    pass


if __name__ == '__main__':
    number = int(get_number())
    print(number)
    new_list = [i for i in create_list(number) if number % i == 0]
    print(*new_list)
