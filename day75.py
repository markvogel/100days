from day65 import test
import re


def double_char(str):
    new_str = ''
    for i in str:
        new_str += i * 2
    return new_str


# def count_code(str):
#     count = 0
#     for i in range(str.count("co")):
#         a = str.find("co", count)
#         if str[a + 3] == "e":
#             count += 1
#     return count


def count_code(str):
    return len([s.start() for s in re.finditer('co[a-z]e', str)])
    # [0, 5, 10, 15]


# without regex - http://gregorulm.com/coding-bat-python-string-2/
# def count_code(str):
#     count = 0
#     for i in range(0, len(str) - 3):
#         if str[i:i + 2] == 'co' and str[i + 3] == 'e':
#             count += 1
#     return count


def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'i' and str[i - 1] == 'h':
            count += 1
    return count


def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


def cat_dog(str):
    return str.count('cat') == str.count('dog')


def xyz_there(str):
    return str[str.index('xyz') - 1] != '.'


def test_suite():
    test(double_char('The') == 'TThhee')
    test(double_char('AAbb') == 'AAAAbbbb')
    test(double_char('Hi-There') == 'HHii--TThheerree')
    test(count_code('aaacodebbb') == 1)
    test(count_code('codexxcode') == 2)
    test(count_code('cozexxcope') == 2)
    test(count_code('aaacodebbb') == 1)
    test(count_code('codexxcode') == 2)
    test(count_code('cozexxcope') == 2)
    test(count_code('cozfxxcope') == 1)
    test(count_code('xxcozeyycop') == 1)
    test(count_code('cozcop') == 0)
    test(count_code('abcxyz') == 0)
    test(count_code('code') == 1)
    test(count_code('ode') == 0)
    test(count_code('c') == 0)
    test(count_code('') == 0)
    test(count_code('AAcodeBBcoleCCccoreDD') == 3)
    test(count_code('AAcodeBBcoleCCccorfDD') == 2)
    test(count_code('coAcodeBcoleccoreDD') == 3)
    test(count_hi('abc hi ho') == 1)
    test(count_hi('ABChi hi') == 2)
    test(count_hi('hihi') == 2)
    test(end_other('Hiabc', 'abc'))
    test(end_other('AbC', 'HiaBc'))
    test(end_other('abc', 'abXabc'))
    test(cat_dog('catdog'))
    test(not cat_dog('catcat'))
    test(cat_dog('1cat1cadodog'))
    test(xyz_there('abcxyz'))
    test(not xyz_there('abc.xyz'))
    test(xyz_there('xyz.abc'))


if __name__ == '__main__':
    test_suite()
