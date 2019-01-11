# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

test_list = [1, 3, 5, 30, 42, 43, 500]
test_num = 500


def function_name(a: int, b: list):
    return b in a


def binary_search(number_to_find: int, list_to_search: list):
    middle_index = (len(list_to_search) // 2)
    middle = list_to_search[middle_index]
    print(number_to_find, middle, middle_index)
    if number_to_find == middle:
        return True
    if number_to_find > middle:
        list_to_search = list_to_search[middle_index:]
    if number_to_find < middle:
        list_to_search = list_to_search[:middle_index]
    binary_search(number_to_find, list_to_search)


if __name__ == '__main__':
    # if function_name(test_num, test):
    #     print('True')
    if binary_search(test_num, test_list):
        print('awesome')
