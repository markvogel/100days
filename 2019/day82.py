from under100.day65 import test
import string

watts = """Trying to define yourself is like trying to bite your own teeth."""


def test_suite():
    test(count_letters("banana", "a") == 3)


def count_letters(a_str, a_ltr):
    count = 0
    for i in a_str:
        if i == a_ltr:
            count += 1
    return count


def count_e(a_str):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    a_list = a_str.translate(table).split()
    e_words = 0
    for word in a_list:
        if "e" in word:
            e_words += 1
    n_words = len(a_list)
    e_percent = round((e_words / n_words) * 100)
    print(f"Your text contains {n_words} words, of which {e_words} ({e_percent}%) contain an \"e\".")


if __name__ == '__main__':
    test_suite()
    with open("sowpods.txt") as file:
        a = file.read()
        a = a.lower()
        count_e(a)
