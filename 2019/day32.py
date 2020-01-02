# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random
import string

PASS = ['hello', 'world', 'passwords', 'should', 'be', 'secure', 'and', 'not', 'very', 'simple']


def password_generator():
    password_strength = strength()
    if password_strength == 'weak':
        return str(weak() + weak())
    elif password_strength == 'strong':
        return strong()


def strength():
    p = ''
    while p != 'weak' and p != 'strong':
        p = input('How strong would you like your password to be? Please specify (weak or strong): ')
    return p


def weak():
    return PASS[random.randint(0, len(PASS) - 1)]


def strong():
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(8, 16))])


def more_passwords():
    return input('Would you like to generate another password? Please indicate yes or no: ')


def app():
    print('Welcome to the password generator!')


if __name__ == '__main__':
    app()
    print(password_generator())
    while more_passwords() == 'yes':
        print(password_generator())
