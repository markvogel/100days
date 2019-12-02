# https://adventofcode.com/2019/day/1
import puzzle_input


def fuel_required(module):
    return (int(module) // 3) - 2


def fuel_required2(module):
    fuel = 0
    while module // 3 > 0:
        fuel += (module // 3) - 2
    return fuel


def part2(module):
    print(module, fuel_required(module))


if __name__ == '__main__':
    modules = puzzle_input.day_1.split()
    total = 0
    for i in modules:
        current = fuel_required(i)
        total += current
        while current > 0:
            fuel_required(current)
            print(current)
        total += current
    print(total)
