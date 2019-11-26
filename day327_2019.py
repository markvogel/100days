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


def reverse(text):
    r = ""
    for c in range(1, len(text) + 1):
        r += text[-c]
    return r


def anti_vowel(text):
    vowels = ["a", "e", "i", "o", "u"]
    new_text = ''
    for c in text:
        if c.lower() not in vowels:
            new_text += c
    return new_text
