# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]
z = []


def list_ends(b: list):
    return [b.pop(0), b.pop()]


# solution given on website
def list_ends2(c: list):
    return [c[0], c[len(c) - 1]]


def get_number():
    return int(input('Please enter a number: '))


def fibonacci(number: int):
    list1 = []
    if number == 0:
        list1 = [0]
    elif number == 1:
        list1 = [1]
    else:
        list1 = [1, 1]
        for x in range(number):
            list1.append(list1[-2] + list1[-1])
        return list1


if __name__ == '__main__':
    print(fibonacci(get_number()))
