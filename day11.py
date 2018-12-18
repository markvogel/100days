# Comma code practice project from  http://automatetheboringstuff.com/chapter4/

spam = ['apples', 'bananas', 'tofu', 'cats']
numbers = [1, 2, 3, 4, 5, 6]


def function_fun(list_input):
    combined_string = ''
    for i in range(len(list_input)):
        if list_input[i] == list_input[len(list_input) - 1]:
            # combined_string += f'and {list_input[i]}.'
            combined_string += 'and ' + str(list_input[i])

            break
        combined_string += f'{list_input[i]}, '
    return combined_string


if __name__ == '__main__':
    print(function_fun(numbers))
