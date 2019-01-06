# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

sample = 'My name is Mark'


def reverse_word_order(a: str):
    split_list = a.split()
    last_word = split_list.pop()
    split_list.insert(0, last_word)
    return ' '.join(split_list).capitalize()


if __name__ == '__main__':
    print(reverse_word_order(sample))
