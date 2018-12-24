# https://adventofcode.com/2018/day/1
starting_frequency = 0
example1 = [1, -2, 3, 1]
example2 = [1, 1, 1]
example3 = [1, 1, -2]
example4 = [-1, -2, -3]


def calc_freq(changes: list):
    freq = starting_frequency
    for i in changes:
        freq += int(i)
    return freq


if __name__ == '__main__':
    print(calc_freq(example1) == 3)
    print(calc_freq(example2) == 3)
    print(calc_freq(example3) == 0)
    print(calc_freq(example4) == -6)
    total_freq = calc_freq(example1) + calc_freq(example2) + calc_freq(example3) + calc_freq(example4)
    print(total_freq)
