# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/


test = '03600029145'


def convert_to_list(a: str):
    return [int(i) for i in a]


def add_evens(b: list):
    return b[0] + b[2] + b[4] + b[6] + b[8] + b[10]


def step2(c: int):
    return c * 3


def add_odds(d: list):
    return d[1] + d[3] + d[5] + d[7] + d[9]


def step4(e: int):
    return e % 10


def upc(f: str):
    check_digit = None
    x = convert_to_list(f)
    y = step4(step2(add_evens(x)) + add_odds(x))
    if not y:
        check_digit = 0
    if y:
        check_digit = 10 - y
    return check_digit


if __name__ == '__main__':
    print(upc('07732683092'))
