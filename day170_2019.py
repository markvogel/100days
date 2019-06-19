# https://www.py4e.com/html3/08-lists


# exercise 1
def chop(list1: list):
    del list1[0], list1[-1]


def middle(list2):
    return list2[1:-1]


# a line in a text file with only "From" on it will break this program
def e2():
    infile = open('test.txt')
    count = 0
    for line in infile:
        words = line.split()
        # print 'Debug:', words
        if len(words) == 0 and words[0] != 'From':
            continue
        # if words[0] != 'From': continue
        print(words[2])


if __name__ == '__main__':
    # letters = ['a', 'b', 'c']
    # chop(letters)
    # print(letters)
    # print(middle(letters))
    e2()
