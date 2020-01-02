# building off of yesterday, create a simple program to check if a word is the same forwards as backwards (palindrome)


def reverse_string(input_string):
    return input_string[::-1]


def palindrome_check(input_string):
    if input_string == reverse_string(input_string):
        return True
    return False


if __name__ == '__main__':
    s = str(input('please enter a string: '))
    if palindrome_check(s):
        print('you entered a palindrome')
    else:
        print('alas, the string you entered is not a palindrome')
