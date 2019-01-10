# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
import random

random_4digit = str(random.randint(0, 9999))


def get_number():
    guess = ''
    while len(guess) != 4:
        guess = input('Please enter a number: ')
    return guess


def cows_bulls(num1: str):
    cows, bulls = 0, 0
    for c in range(len(num1)):
        if num1[c] == random_4digit[c]:
            cows += 1
        elif num1[c] in random_4digit:
            bulls += 1
    return cows, bulls


def print_cows_bulls(x, y):
    print(f'{x} cows, {y} bulls')


if __name__ == '__main__':
    print('Welcome to the Cows and Bulls Game!')
    x, y = cows_bulls(get_number())
    print_cows_bulls(x, y)
    guesses = 1
    while x < 4:
        x, y = cows_bulls(get_number())
        print_cows_bulls(x, y)
        guesses += 1
    print(f'You guessed {guesses} times before you guessed the number.')
