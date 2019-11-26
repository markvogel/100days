# Exercise 3
# https://www.py4e.com/html3/09-dictionaries
from pprint import pprint


def mail_log():
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
                sender = words[1]
                if sender not in w_dict:
                    w_dict.setdefault(sender, 1)
                    continue
                if words[1] in w_dict:
                    w_dict[sender] = w_dict[sender] + 1
        except IndexError:
            continue
    pprint(w_dict)


if __name__ == '__main__':
    mail_log()
