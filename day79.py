import math

from day65 import test


def is_multiple(n, m):
    return not n % m


def f2c(t):
    return round((t - 32) * (5 / 9))


def c2f(t):
    return round(t * (9 / 5) + 32)


def count_odds(a_list):
    count = 0
    for i in a_list:
        if i % 2:
            count += 1
    return count


def count_odds2(a_list):
    return len([i for i in a_list if i % 2])


def sum_evens(a_list):
    return sum([i for i in a_list if not i % 2])


def sum_odds(a_list):
    return sum([i for i in a_list if i % 2])


def count_len_5(a_list):
    return len([i for i in a_list if len(i) == 5])


def sum_list(a_list):
    total = 0
    for i in a_list:
        if not i % 2:
            break
        total += i
    return total


def sum_sam_list(a_list):
    total = 0
    for i in a_list:
        if i == 'sam':
            break
        total += 1
    return total


def sqrt(n):
    approx = n / 2.0  # Start with some or other guess at the answer
    while True:
        better = (approx + n / approx) / 2.0
        print(f'better = ' + str(better))
        if abs(approx - better) < 0.001:
            return better
        approx = better


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, high)


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(n * i, end="   ")
    print()


def print_triangular_numbers(n):
    for i in range(1, n + 1):
        print(round((i * (i + 1)) / 2))


def is_prime(n):
    for i in range(2, n):
        if not (n % i):
            return False
    return True


def test_suite():
    # test(is_multiple(12, 3))
    # test(is_multiple(12, 4))
    # test(not is_multiple(12, 5))
    # test(is_multiple(12, 6))
    # test(not is_multiple(12, 7))
    # test(f2c(212) == 100)  # Boiling point of water
    # test(f2c(32) == 0)  # Freezing point of water
    # test(f2c(-40) == -40)  # Wow, what an interesting case!
    # test(f2c(36) == 2)
    # test(f2c(37) == 3)
    # test(f2c(38) == 3)
    # test(f2c(39) == 4)
    # test(c2f(0) == 32)
    # test(c2f(100) == 212)
    # test(c2f(-40) == -40)
    # test(c2f(12) == 54)
    # test(c2f(18) == 64)
    # test(c2f(-48) == -54)
    # test(count_odds2(range(6)) == 3)
    # test(count_odds2(range(12)) == 6)
    # test(count_odds2([2, 4, 6, 8, 10]) == 0)
    # test(sum_evens([2, 4, 6, 8, 10]) == 30)
    # test(sum_evens([]) == 0)
    # test(sum_evens([2, 4, 6]) == 12)
    # test(sum_odds([1, 3, 5]) == 9)
    # test(sum_odds([2, 4, 6]) == 0)
    # test(sum_odds([2, 4, 6, 1]) == 1)
    # test(count_len_5(['abcde']) == 1)
    # test(count_len_5(['']) == 0)
    # test(count_len_5(['abcde', 'abcde', 'abcde', 'abcde', 'abcde']) == 5)
    # test(sum_list([1, 3, 5]) == 9)
    # test(sum_list([1, 2, 3, 5]) == 1)
    # test(sum_list([1, 1, 1, 1, 1, 2, 3, 5]) == 5)
    # test(sum_sam_list(['sam', 'john', 'allison', 'tom']) == 0)
    # test(sum_sam_list(['', 'john', 'allison', 'tom', 'sam']) == 4)
    # test(sum_sam_list(['john', 'allison', 'tom', 'john', 'allison', 'tom']) == 6)
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


if __name__ == '__main__':
    test_suite()
    # sqrt(25)
    # print_mult_table(7)
    # print_triangular_numbers(5)
