# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
import random


def open_sowpods():
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def random_word(a: list):
    return random.choice(a)


if __name__ == '__main__':
    print(random_word(open_sowpods()))
