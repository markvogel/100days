from day65 import test


def hello_name(name):
    # return f'Hello {name}!'
    return 'Hello {}!'.format(name)


def make_out_word(out, word):
    return out[:2] + word + out[2:]


def first_half(str):
    return str[:(int(len(str) / 2))]


def non_start(a, b):
    return a[1:] + b[1:]


def make_abba(a, b):
    return a + b + b + a


def extra_end(str):
    return str[-2:] * 3


def without_end(str):
    return str[1:-1]


def left2(str):
    return str[2:] + str[:2]


def make_tags(tag, word):
    return '<{}>{}</{}>'.format(tag, word, tag)


def first_two(str):
    if len(str) < 2:
        return str
    return str[:2]


def combo_string(a, b):
    max_str, min_str = a, b
    if len(b) > len(a):
        max_str, min_str = b, a
    return min_str + max_str + min_str


def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def reverse3(nums):
    return [nums[-1], nums[-2], nums[-3]]


def middle_way(a, b):
    return [a[1], b[1]]


def same_first_last(nums):
    if len(nums):
        if nums[0] == nums[-1]:
            return True
    return False


def sum3(nums):
    return sum(nums)


def test_suite():
    test(hello_name('Bob') == 'Hello Bob!')
    test(hello_name('Alice') == 'Hello Alice!')
    test(hello_name('X') == 'Hello X!')
    test(make_out_word('<<>>', 'Yay') == '<<Yay>>')
    test(make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>')
    test(make_out_word('[[]]', 'word') == '[[word]]')
    test(first_half('WooHoo') == 'Woo')
    test(first_half('HelloThere') == 'Hello')
    test(first_half('abcdef') == 'abc')
    test(non_start('Hello', 'There') == 'ellohere')
    test(non_start('java', 'code') == 'avaode')
    test(non_start('shotl', 'java') == 'hotlava')
    test(make_abba('Hi', 'Bye') == 'HiByeByeHi')
    test(make_abba('Yo', 'Alice') == 'YoAliceAliceYo')
    test(make_abba('What', 'Up') == 'WhatUpUpWhat')
    test(extra_end('Hello') == 'lololo')
    test(extra_end('ab') == 'ababab')
    test(extra_end('Hi') == 'HiHiHi')
    test(without_end('Hello') == 'ell')
    test(without_end('java') == 'av')
    test(without_end('coding') == 'odin')
    test(left2('Hello') == 'lloHe')
    test(left2('java') == 'vaja')
    test(left2('Hi') == 'Hi')
    test(make_tags('i', 'Yay') == '<i>Yay</i>')
    test(make_tags('i', 'Hello') == '<i>Hello</i>')
    test(make_tags('cite', 'Yay') == '<cite>Yay</cite>')
    test(first_two('Hello') == 'He')
    test(first_two('abcdefg') == 'ab')
    test(first_two('ab') == 'ab')
    test(combo_string('Hello', 'hi') == 'hiHellohi')
    test(combo_string('hi', 'Hello') == 'hiHellohi')
    test(combo_string('aaa', 'b') == 'baaab')
    test(first_last6([1, 2, 6]))
    test(first_last6([6, 1, 2, 3]))
    test(not first_last6([13, 6, 1, 2, 3]))
    test(common_end([1, 2, 3], [7, 3]))
    test(not common_end([1, 2, 3], [7, 3, 2]))
    test(common_end([1, 2, 3], [1, 3]))
    test(reverse3([1, 2, 3]) == [3, 2, 1])
    test(reverse3([5, 11, 9]) == [9, 11, 5])
    test(reverse3([7, 0, 0]) == [0, 0, 7])
    test(middle_way([1, 2, 3], [4, 5, 6]) == [2, 5])
    test(middle_way([7, 7, 7], [3, 8, 0]) == [7, 8])
    test(middle_way([5, 2, 9], [1, 4, 5]) == [2, 4])
    test(not same_first_last([1, 2, 3]))
    test(same_first_last([1, 2, 3, 1]))
    test(same_first_last([1, 2, 1]))
    test(sum3([1, 2, 3]) == 6)
    test(sum3([5, 11, 2]) == 18)
    test(sum3([7, 0, 0]) == 7)


if __name__ == '__main__':
    test_suite()
