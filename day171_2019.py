# https://www.py4e.com/html3/09-dictionaries
from pprint import pprint


def read_words():
    w_dict = {}
    infile = open('words.txt')
    # count = 0
    for line in infile:
        words = line.split()
        # print 'Debug:', words
        for word in words:
            if word not in w_dict:
                w_dict.setdefault(word, None)
    pprint(w_dict)


if __name__ == '__main__':
    read_words()
