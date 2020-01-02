from under100.day65 import test
import numpy as np


def spiral_transposition2(matrix):
    matrix = np.array(matrix)
    a = matrix.flatten()
    return a.tolist()


def spiral_transposition3(matrix):
    new_array = []
    for i in range(len(matrix)):
        if not (i % 2):
            new_array.append(matrix[i])
            continue
        new_array.append(matrix[i][::-1])
    new_array = np.array(new_array)
    b = new_array.flatten()
    return b.tolist()


def spiral_transposition(array):
    new_array = []
    for i in range(len(array)):
        for ii in range(len(array)):
            if i == 0:
                new_array.append(array[i][ii])


def test_suite():
    test(
        spiral_transposition(
            [
                [7, 2],
                [5, 0]
            ]
        ) ==
        [7, 2, 0, 5]
    )

    test(
        spiral_transposition(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        ) ==
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    )

    test(
        spiral_transposition(
            [
                [1, 9, 9],
                [2, 4, 9],
                [7, 3, 9]
            ]
        ) ==
        [1, 9, 9, 9, 9, 3, 7, 2, 4]
    )

    test(
        spiral_transposition(
            [
                [6, 4, 3, 9],
                [2, 5, 7, 1],
                [8, 6, 2, 3],
                [4, 5, 9, 1]
            ]
        ) ==
        [6, 4, 3, 9, 1, 3, 1, 9, 5, 4, 8, 2, 5, 7, 2, 6]
    )

    test(
        spiral_transposition(
            [
                [4, 1, 55, 5, 9],
                [16, 7, 6, 5, 3],
                [8, 20, 2, 0, 8],
                [2, 9, 9, 1, 11],
                [6, 5, 3, 18, 5]
            ]
        ) ==
        [4, 1, 55, 5, 9, 3, 8, 11, 5, 18, 3, 5, 6, 2, 8, 16, 7, 6, 5, 0, 1, 9, 9, 20, 2]
    )

    test(
        spiral_transposition(
            [
                [1, 5],
                [9, 2],
                [7, 3]
            ]
        ) ==
        [1, 5, 2, 3, 7, 9]
    )

    test(
        spiral_transposition(
            [
                [2, 4, 6, 8],
                [7, 3, 0, 5]
            ]
        ) ==
        [2, 4, 6, 8, 5, 0, 3, 7]
    )


if __name__ == '__main__':
    test_suite()
    print(spiral_transposition(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))
    print(spiral_transposition([
        [2, 4, 6, 8],
        [7, 3, 0, 5]
    ]))
