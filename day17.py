# https://adventofcode.com/2018/day/1
starting_frequency = 0
example1 = [1, -2, 3, 1]
example2 = [1, 1, 1]
example3 = [1, 1, -2]
example4 = [-1, -2, -3]
example5 = [1, 1, -2]

e1 = [1, -1]
e2 = [3, 3, 4, -2, -4]
e3 = [-6, 3, 8, 5, -6]
e4 = [7, 7, -2, -7, -4]


def calc_freq(changes: list):
    freq = starting_frequency
    for i in changes:
        freq += int(i)
    return freq


if __name__ == '__main__':
    print(sum(e1))
