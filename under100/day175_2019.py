# Exercise 4
# https://www.py4e.com/html3/09-dictionaries
from pprint import pprint


def mail_log():
    w_dict = {}
    infile = open('mbox.txt')
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
    top = max(w_dict)
    print(f"{top}: {w_dict.get(top)}")


def mail_log2():
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
                sender_domain = words[1].split(sep="@")[1]
                if sender_domain not in w_dict:
                    w_dict.setdefault(sender_domain, 1)
                    continue
                if sender_domain in w_dict:
                    w_dict[sender_domain] = w_dict[sender_domain] + 1
        except IndexError:
            continue
    pprint(w_dict)
    top = max(w_dict)
    print(f"{top}: {w_dict.get(top)}")


if __name__ == '__main__':
    # mail_log()
    mail_log2()
