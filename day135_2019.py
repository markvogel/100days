from under100.day65 import test


def show_numbers(limit):
    nums = [i for i in range(limit + 1)]
    for num in nums:
        odd_even(num)


def odd_even(num):
    if num % 2:
        print(str(num) + " ODD")
    print(str(num) + " EVEN")


def sum_three_five(limit):
    nums = [i for i in range(limit + 1) if not i % 3 or not i % 5]
    return sum(nums)


def show_stars(rows):
    rows = [i for i in range(1, rows + 1)]
    for i in rows:
        print("*" * i)


def print_primes(limit):
    r = [i for i in range(limit + 1)]


def test_suite():
    test(sum_three_five(20) == 98)
    test(sum_three_five(3) == 3)
    test(sum_three_five(5) == 8)
    test(sum_three_five(0) == 0)


if __name__ == '__main__':
    test_suite()
    # show_numbers(20)
    # show_stars(5)
