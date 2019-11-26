"""Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method"""

nums = range(2000, 3201)


def foo():
    working_nums = [i for i in nums]
    a = []
    for num in working_nums:
        if not (num % 7) and num % 5:
            a.append(num)
    print(a)


if __name__ == '__main__':
    foo()
