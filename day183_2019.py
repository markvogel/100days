# https://www.py4e.com/html3/10-tuples
import string
import pprint


# Exercise 3
def letters():
    l_dict = {}
    infile = open('mbox-short.txt')
    for line in infile:
        line = line.lower().strip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.translate(str.maketrans('', '', string.whitespace))
        for char in line:
            if char not in l_dict:
                l_dict.setdefault(char, 1)
                continue
            if char in l_dict:
                l_dict[char] += 1
        # print(line)
    # if len(words) == 0 and 'From' not in words:
    #     continue
    # # if words[0] != 'From': continue
    # try:
    #     if words[0] == 'From':
    #         sender = words[1]
    #         if sender not in w_dict:
    #             w_dict.setdefault(sender, 1)
    #             continue
    #         if words[1] in w_dict:
    #             w_dict[sender] = w_dict[sender] + 1
    # except IndexError:
    #     continue

    # top = max(w_dict)
    # print(f"{top}: {w_dict.get(top)}")
    # # sender_list = sorted(list(w_dict.items()), reverse=True)
    # sender_list = sorted([(v, k) for k, v in w_dict.items()], reverse=True)
    pprint.pprint(l_dict)


if __name__ == '__main__':
    letters()
