from under100.day65 import test
import string

exclude = set(string.punctuation)


# https://edabit.com/challenge/xmyNqzxAgpE47zXEt
def is_alphabetically_sorted(a_str):
    word_list = a_str.split()
    for word in word_list:
        if len(word) < 3:
            continue
        word = ''.join(ch for ch in word if ch not in exclude)
        if word == ''.join(sorted(word)):
            return True
    return False


# https://edabit.com/challenge/rj7E4k6vSNZ9KpT9c
def factor_chain(num_list):
    for i in range(len(num_list)):
        if i == len(num_list) - 1:
            return True
        if num_list[i + 1] % num_list[i]:
            return False
    return True


def test_suite():
    test(is_alphabetically_sorted("Paula has a French accent."))
    # "accent" is alphabetically sorted.
    test(is_alphabetically_sorted("The biopsy returned negative results."))
    # "biopsy" is alphabetically sorted.
    test(not is_alphabetically_sorted("She sells sea shells by the sea shore."))
    # Although "by" is alphabetically sorted, it is only 2 letters long.
    test(is_alphabetically_sorted('Paula has a French accent.'))
    test(is_alphabetically_sorted('The biopsy returned negative results.'))
    test(not is_alphabetically_sorted('She sells sea shells by the sea shore.'))
    test(is_alphabetically_sorted('She almost reached the top of Mt. Everest.'))
    test(is_alphabetically_sorted('She was happy with how her earring hoops looked.'))
    test(not is_alphabetically_sorted('Beth dislikes eating starfruit but enjoys cherries.'))
    test(is_alphabetically_sorted("Elinor is inside on a rainy day sipping hot chocolate."))
    test(not is_alphabetically_sorted("Mara took a photograph."))
    test(factor_chain([1, 2, 4, 8, 16, 32]))
    test(factor_chain([1, 1, 1, 1, 1, 1]))
    test(not factor_chain([2, 4, 6, 7, 12]))
    test(not factor_chain([10, 1]))
    test(break_point(159780))
    test(break_point(112))
    test(break_point(1034))
    test(not break_point(10))
    test(not break_point(343))


if __name__ == '__main__':
    test_suite()
