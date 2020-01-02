# https://www.py4e.com/html3/08-lists
from pprint import pprint


# exercise 1
def chop(list1: list):
    del list1[0], list1[-1]


def middle(list2):
    return list2[1:-1]


# a line in a text file with only "From" on it will break this program
# Exercise 2 and 3
def e2():
    infile = open('mbox-short.txt')
    # count = 0
    for line in infile:
        words = line.split()
        # print 'Debug:', words
        if len(words) == 0 and 'From' not in words:
            continue
        # if words[0] != 'From': continue
        try:
            if words[0] == 'From':
                print(words[1])
        except IndexError:
            continue


# Exercise 4
def e4():
    infile = open('romeo.txt')
    # count = 0
    a_list = []
    for line in infile:
        words = line.split()
        # print 'Debug:', words
        a_list.extend(words)
        # for i in words:
        #     if i not in a_list:
        #         a_list.append(i)
    a_list = set(a_list)
    a_list = sorted(a_list)
    # a_list.sort()
    print(a_list)


# Exercise 5
def e5():
    infile = open('mbox-short.txt')
    # count = 0
    senders = []
    for line in infile:
        words = line.split()
        # print 'Debug:', words
        if len(words) == 0 and 'From' not in words:
            continue
        # if words[0] != 'From': continue
        try:
            if words[0] == 'From':
                senders.append(words[1])
                print(words[1])
        except IndexError:
            continue
    # pprint(senders)
    print(f"There were {len(senders)} lines in the file with From as the first word")


# Exercise 6
def e6():
    num_list = []
    num = None
    while num != "done":
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            num = float(num)
            num_list.append(num)
        except ValueError:
            print("Invalid input")
            print(num_list)
            e6()
    print(f"Maximum: {max(num_list)}")
    print(f"Minimum: {min(num_list)}")


if __name__ == '__main__':
    # letters = ['a', 'b', 'c']
    # chop(letters)
    # print(letters)
    # print(middle(letters))
    # e2()
    # e4()
    e6()
