# Day 22: Mode Maze
# https://adventofcode.com/2018/day/22


def erosion_level(index: int, depth: int):
    return (index + depth) % 20183


def calc_type(erosion_lvl: int):
    return erosion_lvl % 3


def geo_index(coordinates: list, target: list):
    x = coordinates[0]
    y = coordinates[1]
    if coordinates == target or coordinates == [0, 0]:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    else:
        return erosion_level(geo_index([x - 1, y], target), 510) \
               * erosion_level(geo_index([x, y - 1], target), 510)


# depth, coordinates
scan = [510, [10, 10]]

if __name__ == '__main__':
    risk = 0
    for i in range(10):
        g_index = geo_index([i, 0], [10, 10])
        g_index2 = geo_index([0, i], [10, 10])
        risk += calc_type(erosion_level(g_index, 510))
        risk += calc_type(erosion_level(g_index2, 510))
    print(risk)
