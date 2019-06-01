import random


# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
def list_ends(lst):
    if len(lst) == 0:
        return lst
    return [lst[0], lst[-1]]


# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
def guessing_game_one():
    num = random.randint(1, 9)
    guess = 0
    c = 0
    while guess != num:
        c += 1
        guess = int(input("I'm thinking of a number from 1 to 9, please guess it: "))
    print(f"It took you {c} guesses to guess my number, which was {num}!")


if __name__ == '__main__':
    # a = [5, 10, 15, 20, 25]
    # print(list_ends(a))
    # print(list_ends([]))
    guessing_game_one()
