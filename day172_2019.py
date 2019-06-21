# https://www.py4e.com/html3/09-dictionaries
from pprint import pprint
import collections


# Exercise 2
def dow():
    w_dict = {}
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
                t = words[2]
                if t not in w_dict:
                    w_dict.setdefault(t, 1)
                    continue
                if words[2] in w_dict:
                    w_dict[t] = w_dict[t] + 1
        except IndexError:
            continue
    pprint(w_dict)


if __name__ == '__main__':
    dow()
