def is_prime(x):
    if x < 0:
        return False
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    for n in range(2, x - 1):
        if (x % n) == 0:
            return False
    return True
