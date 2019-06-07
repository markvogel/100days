def check_primality(num2):
    if len(divisors(num2)) <= 1:
        return 'prime'
    else:
        return 'not prime'


def divisors(num1):
    num_range = [i for i in range(1, num1)]
    d = [i for i in num_range if not num1 % i]
    return d


if __name__ == '__main__':
    num = int(input("Please enter a number: "))
    print(check_primality(num))
