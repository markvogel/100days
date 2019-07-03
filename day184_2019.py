# https://www.py4e.com/html3/11-regex
import re


# exercise 1
def grep():
    return input("Enter a regular expression: ")


def runner(a_regex='^From'):
    file_name = 'mbox.txt'
    hand = open(file_name)
    count = 0
    for line in hand:
        x = re.findall(a_regex, line)
        if x:
            count += 1
    print(f"{file_name} had {count} lines that matched {a_regex}")


# hand = open('mbox-short.txt')
# count = 0
# for line in hand:
#     x = re.findall(a_regex, line)
#     if x:
#         count += 1
# print(count)


# Code: http://www.py4e.com/code3/re12.py


if __name__ == '__main__':
    runner(grep())
