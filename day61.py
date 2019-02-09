import sys
import json

with open("info.json", "r") as f:
    info = json.load(f)


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(get_bday("") == "")


def welcome():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in info.keys():
        print(i)


def get_bday(a: str):
    return "{}'s birthday is {}.".format(a, info.get(a, "not stored"))


if __name__ == '__main__':
    test_suite()
    # welcome()
    # x = input("Who's birthday do you want to look up?")
    # print(get_bday(x))
