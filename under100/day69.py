# https://codingbat.com/python/Warmup-2

from under100.day65 import test


def string_times(str1, n):
    return str1 * n


def string_splosion(str2):
    out = ''
    for i in range(len(str2) + 1):
        out = out + str2[:i]
    return out


def array_front9(nums):
    for i in nums[:4]:
        if i == 9:
            return True
    return False


def front_times(str3, n):
    if len(str3) < 4:
        return str3 * n
    return str3[:3] * n


def last2(str):
    count = 0
    if len(str) == 0:
        return count
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == str[-2:]:
            count = count + 1
    return count


def array123(nums):
    nums = ''.join([str(i) for i in nums])
    return '123' in nums


def string_bits(str4):
    new_str = ''
    for i in range(len(str4)):
        if not i % 2:
            new_str += str4[i]
    return new_str


def array_count9(nums):
    return nums.count(9)


def string_match(a, b):
    count = 0
    for i in range(len(a) - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count


def test_suite():
    test(string_times('Hi', 2) == 'HiHi')
    test(string_times('Hi', 3) == 'HiHiHi')
    test(string_times('Hi', 1) == 'Hi')
    test(string_splosion('Code') == 'CCoCodCode')
    test(string_splosion('abc') == 'aababc')
    test(string_splosion('ab') == 'aab')
    test(array_front9([1, 2, 9, 3, 4]))
    test(not array_front9([1, 2, 3, 4, 9]))
    test(not array_front9([1, 2, 3, 4, 5]))
    test(front_times('Chocolate', 2) == 'ChoCho')
    test(front_times('Chocolate', 3) == 'ChoChoCho')
    test(front_times('Abc', 3) == 'AbcAbcAbc')
    test(last2('hixxhi') == 1)
    test(last2('xaxxaxaxx') == 1)
    test(last2('axxxaaxx') == 2)
    test(array123([1, 1, 2, 3, 1]))
    test(not array123([1, 1, 2, 4, 1]))
    test(array123([1, 1, 2, 1, 2, 3]))
    test(string_bits('Hello') == 'Hlo')
    test(string_bits('Hi') == 'H')
    test(string_bits('Heeololeo') == 'Hello')
    test(array_count9([1, 2, 9]) == 1)
    test(array_count9([1, 9, 9]) == 2)
    test(array_count9([1, 9, 9, 3, 9]) == 3)
    test(string_match('xxcaazz', 'xxbaaz') == 3)
    test(string_match('abc', 'abc') == 2)
    test(string_match('abc', 'axc') == 0)


if __name__ == '__main__':
    test_suite()
