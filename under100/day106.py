from under100.day65 import test


def currently_winning(scores):
    y = [scores[i] for i in range(len(scores)) if not i % 2]
    o = [scores[i] for i in range(len(scores)) if i % 2]
    winning = []
    for i in range(len(y)):
        if y[i] == o[i]:
            winning.append("T")
        elif y[i] > o[i]:
            winning.append("Y")
        elif y[i] < o[i]:
            winning.append("O")
    return winning


def longest_run(lst):
    for c, v in enumerate(lst, 1):
        if v != lst[c - 1] + 1:
            break
        print(c)


def test_suite():
    test(currently_winning([10, 10, 22, 30, 5, 40]) == ["T", "O", "O"])
    test(currently_winning([5, 1, 2, 10]) == ["Y", "O"])
    test(currently_winning([10, 10, 5, 5, 2, 2, 1, 3, 100, 5]) == ["T", "T", "T", "O", "Y"])
    test(longest_run([1, 2, 3, 10, 11, 15]) == 3)
    # Longest consecutive-run: [1, 2, 3].
    test(longest_run([5, 4, 2, 1]) == 2)
    # Longest consecutive-run: [5, 4] and [2, 1].
    test(longest_run([3, 5, 7, 10, 15]) == 1)
    # No consecutive runs, so we return 1.


if __name__ == '__main__':
    test_suite()
