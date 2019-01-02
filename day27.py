# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html


def list_comprehension():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    b = [x for x in a if x % 2 == 0]

    print(a, b)

# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

def test_app():
    player1 = ''
    player2 = ' '
    while player1 not in ['rock', 'paper', 'scissors']:
        player1 = input('Player 1 please choose rock, paper or scissors: ')
    while player2 not in ['rock', 'paper', 'scissors']:
        player2 = input('Player 2 please choose rock, paper or scissors: ')


def rps(name: str):
    s = ''
    while s not in ['rock', 'paper', 'scissors']:
        s = input(f'{name} please choose rock, paper or scissors: ')
    return s


def compare_rps(y, z):
    if y == z:
        return "It's a tie!"
    if y == 'rock' and z == 'scissors':
        return 'P1 Rock beats scissors'
    if y == 'paper' and z == 'rock':
        return 'P1 Paper beats rock'
    if y == 'scissors' and z == 'paper':
        return 'P1 Scissors beats paper'
    if z == 'rock' and y == 'scissors':
        return 'P2 Rock beats scissors'
    if z == 'paper' and y == 'rock':
        return 'P2 Paper beats rock'
    if z == 'scissors' and y == 'paper':
        return 'P2 Scissors beats paper'


def compare_rps2(c, d):
    results1 = {1: ['rock', 'scissors'], 2: ['paper', 'rock'], 3: ['scissors', 'rock']}
    test = [c, d]
    test2 = [d, c]
    if test in results1.values():
        return 'Player 1 wins'
    if test2 in results1.values():
        return 'Player 2 wins'
    return 'It is a tie'


if __name__ == '__main__':
    p1 = rps('Player 1')
    p2 = rps('Player 2')
    print(compare_rps2(p1, p2))
