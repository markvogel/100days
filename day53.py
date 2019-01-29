import sys

sample_list = ['abcdef', 'abcdefghi', 'abc', 'defg', '32145', 'ab1234']
sample_list2 = ['S123456789', '123456789', '  123456789  ', 'S987654321', 'S876543219', 'S765432198']


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def find_like(a: list):
    aaa = []
    for i in a:
        print(i, a)
        a.remove(i)
        for ii in a:
            if i in ii:
                aaa.append([i, ii])
    return aaa


def test_suite():
    test(find_like(sample_list) == [['abcdef', 'abcdefghi'], ['abc', 'abcdefghi']])


if __name__ == '__main__':
    test_suite()
    print(find_like(sample_list))
    # print(find_like(sample_list2))
