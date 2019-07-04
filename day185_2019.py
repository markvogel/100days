# https://www.py4e.com/html3/11-regex
import re


# Exercise 2
def new_revision():
    file_name = 'mbox.txt'
    hand = open(file_name)
    nums = []
    for line in hand:
        x = re.findall('^New Revision: ([0-9]+)', line)
        if len(x):
            nums.extend(x)
    int_nums = [int(i) for i in nums]
    average = sum(int_nums) / len(int_nums)
    print(round(average, ndigits=7))


if __name__ == '__main__':
    new_revision()
