from under100.day65 import test


# https://edabit.com/challenge/QXrpKvEvJA2Yxj2fo
def num_args(*args):
    return len(args)


# https://edabit.com/challenge/TBCujkw9D8hrEgFc4
def validate_email(txt):
    a = txt.split(sep="@")
    if not len(a[0]):
        return False
    if "@" in txt:
        if "." in a[1]:
            return True


def test_suite():
    test(num_args() == 0)
    test(num_args("foo") == 1)
    test(num_args("foo", "bar") == 2)
    test(num_args(True, False) == 2)
    test(num_args({}) == 1)
    test(not validate_email("@gmail.com"))
    test(not validate_email("hello.gmail@com"))
    test(not validate_email("gmail"))
    test(not validate_email("hello@gmail"))
    test(validate_email("hello@edabit.com"))


if __name__ == '__main__':
    test_suite()
