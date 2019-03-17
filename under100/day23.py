# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html


def get_number():
    return input('Please enter a number: ')


def check_num(number):
    starter = 'The number that you entered is '
    if number % 4 == 0:
        return starter + 'a multiple of 4!'
    if number % 2 == 0:
        return starter + 'even'
    return starter + 'odd'


def check_4(number):
    if number % 4 == 0:
        print()


if __name__ == '__main__':
    num1 = ''
    while not num1.isdigit():
        num1 = get_number()
    num2 = int(num1)
    print(check_num(num2))
