# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]
z = []


def list_ends(b: list):
    return [b.pop(0), b.pop()]


# solution given on website
def list_ends2(c: list):
    return [c[0], c[len(c) - 1]]


if __name__ == '__main__':
    print(list_ends(z))
