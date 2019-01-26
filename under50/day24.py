a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def print_less_than_5(list1: list):
    for i in list1:
        if i < 5:
            print(i)


def less_than_num(list1: list, value1: int):
    x = [i for i in list1 if i < value1]
    return x


def get_value_less_than():
    return input('Please enter a value, that you would like to print the list values less than: ')


if __name__ == '__main__':
    print(*less_than_num(a, int(get_value_less_than())))
