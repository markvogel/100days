from under100.day65 import test


# https://edabit.com/challenge/3XtrKPMbxAf86QjjS
def same_case(txt):
    return txt.lower() == txt or txt.upper() == txt


# https://edabit.com/challenge/GoGbZtXDYPDCfeBz8
def magic(txt):
    a = txt.split()
    if a[0] == a[2][-1] and a[1] == a[2][-1]:
        return True
    if a[0] == a[2][-2:] and a[1] == a[2][-2:]:
        return True
    if int(a[0]) * int(a[1]) == int(a[2][-3:]):
        return True

    return False  # "is not a magic date"


def test_suite():
    test(same_case("HELLO"))
    test(not same_case("HEllo"))
    test(not same_case("mArmALadE"))
    test(same_case("marmalade"))
    test(same_case("MARMALADE"))
    test(not same_case("ketchUP"))
    test(same_case("pickle"))
    test(same_case("MUSTARD"))
    test(magic('1 1 2011'))
    test(not magic('4 1 2001'))
    test(magic('2 4 2008'))
    test(magic('3 3 2009'))
    test(magic('5 2 2010'))
    test(not magic('1 2 2011'))
    test(not magic('9 2 2011'))
    test(not magic('1 4 2011'))


if __name__ == '__main__':
    test_suite()
