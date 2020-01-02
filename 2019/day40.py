# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html


def board():
    return int(input('What size game board would you like to draw? (3 for 3x3, 8 for 8x8, etc.'))


def draw_board(a: int):
    for i in range(a):
        draw_piece(' --- ', a)
        draw_piece('|   |', a)
        draw_piece(' --- ', a)


def draw_piece(piece: str, a: int):
    for x in range(a):
        if x == a - 1:
            print(piece, end='\n')
            break
        print(piece, end='')


if __name__ == '__main__':
    draw_board(board())
