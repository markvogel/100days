# https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
from statistics import mean


def hexcolor(a: int, b: int, c: int):
    return '#' + foo(hex(a)) + foo(hex(b)) + foo(hex(c))


def foo(x: str):
    x = x[2:]
    if len(x) < 2:
        x = '0' + x
    return x


def convert_rgb(aa: str):
    return int(aa, 16)


def blend(aaa: list):
    s = []
    for each in aaa:
        s.append([convert_rgb(each[1:3]), convert_rgb(each[3:5]), convert_rgb(each[5:7])])
    return int(mean(s) / 3)


if __name__ == '__main__':
    print(hexcolor(255, 99, 71))
    print(hexcolor(184, 134, 11))
    print(hexcolor(189, 183, 107))
    print(hexcolor(0, 0, 205))
    # print(blend(["#E6E6FA", "#FF69B4", "#B0C4DE"]))
