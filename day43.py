# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html


def max_of_three(a, b, c):
    max1 = None
    if a == b and a == c:
        max1 = a
    if a > b and a > c:
        max1 = a
    if b > a and b > c:
        max1 = b
    if c > a and c > b:
        max1 = c
    return max1


if __name__ == '__main__':
    print(max_of_three(10, 10, 30))
    max(10, 20, 30, 40, 50, )
