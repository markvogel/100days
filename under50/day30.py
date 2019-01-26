# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

sample_list = [1, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def extras_set(a: list):
    return list(set(a))


def extras(a: list):
    new_list = []
    for x in a:
        if x not in new_list:
            new_list.append(x)
    return new_list


def list_overlap(list1: list, list2: list):
    return list(set(list1).intersection(set(list2)))


if __name__ == '__main__':
    print(extras_set(sample_list))
    print(extras(sample_list))
    print(list_overlap(sample_list, c))
