# https://www.hackerrank.com/challenges/swap-case/problem

a = """abcdefghijklmnopqrstuvwxyz"""
b = a.upper()


def swap_case(str1):
    new = []
    for i in range(len(str1)):
        if str1[i] in a:
            new.append(str1[i].upper())
        elif str1[i] in b:
            new.append(str1[i].lower())
    return "".join(new)


if __name__ == '__main__':
    print(swap_case("aAbB"))
