from under100.day65 import test


def num_digits(n):
    n = abs(n)
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count += 1
        n //= 10
    return count


def num_even_digits(n):
    n = abs(n)
    count = 0
    if n == 0:
        return 1
    while n != 0:
        if not n % 2:
            count += 1
        n //= 10
    return count


def sum_of_squares(xs: list):
    return sum([i ** 2 for i in xs])


# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1} ".format(human_plays_first, result))
    return result


def noughts_crosses():
    play_again = 'y'
    c = {-1: 0, 0: 0, 1: 0}
    while play_again == 'y':
        a = play_once(input("Who should play first this game? (1 for human, 0 for computer)"))
        b = {-1: "Human wins!", 0: "Game drawn!", 1: "I win!"}
        print(b.get(a))
        c[a] += 1
        print(f"{b.get(-1)[:-1]}: {c.get(-1)}, {b.get(0)[:-1]}: {c.get(0)}, {b.get(1)[:-1]}: {c.get(1)} ")
        h = round((c.get(-1) / sum(c.values())) * 100)
        print(f"{b.get(-1)[:-1]} percentage = {h}%")
        play_again = input("Would you like to play again? (y or n): ")
    print("Goodbye")


def test_suite():
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


if __name__ == '__main__':
    test_suite()
    # print(num_digits(0))
    noughts_crosses()
