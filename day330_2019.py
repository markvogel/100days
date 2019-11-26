def censor(text, word):
    words = [i for i in text.split()]
    for i in range(len(words)):
        if words[i] == word:
            words[i] = "*" * len(word)
    censored = " ".join(words)
    return censored


def censor2(text, word):
    # words = [i for i in text.split()]
    return " ".join([x if x != word else "*" * len(word) for x in ([i for i in text.split()])])


def count(sequence, item):
    num = 0
    for i in sequence:
        if i == item:
            num += 1
    return num


def count2(sequence, item):
    return sequence.count(item)


if __name__ == '__main__':
    print(censor("this hack is wack hack", "hack"))
    print(censor2("this hack is wack hack", "hack"))
    print(count([1, 2, 1, 1], 1))
    print(count2([1, 2, 1, 1], 1))
