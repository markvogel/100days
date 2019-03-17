# http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html


def test_tuple():
    a = 1, 2, 3, 4
    try:
        print(a.index(5))
    except ValueError:
        print('')


def variables():
    message, n, pi = "What's up, Doc?", 17, 3.15159
    print(message, n, pi)


if __name__ == '__main__':
    variables()
