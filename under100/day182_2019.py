# https://www.py4e.com/html3/10-tuples


# Exercise1
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
    # sender_list = sorted(list(w_dict.items()), reverse=True)
    sender_list = sorted([(v, k) for k, v in w_dict.items()], reverse=True)
    print(sender_list)


# Exercise2
def mail_log2():
    w_dict = {}
    infile = open('mbox-short.txt')
    # count = 0
    for line in infile:
        words = line.split(sep=':')
        # print('Debug:', words)
        if len(words) == 0 and 'From' not in words:
            continue
        # if words[0] != 'From': continue
        try:
            if words[0].startswith('From'):
                hour = words[0][-2:]
                try:
                    int(hour)
                except ValueError:
                    continue
                # print('Debug:', hour)
                if hour not in w_dict:
                    w_dict.setdefault(hour, 1)
                    continue
                if hour in w_dict:
                    w_dict[hour] = w_dict[hour] + 1
        except IndexError:
            continue

    # top = max(w_dict)
    # print(f"{top}: {w_dict.get(top)}")
    hour_list = sorted([(k, v) for k, v in w_dict.items()], reverse=False)
    for each in hour_list:
        print(each)


if __name__ == '__main__':
    mail_log2()
