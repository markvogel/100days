def factorial(x):
    if x == 1:
        return 1
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total


if __name__ == '__main__':
    print(factorial(4))
