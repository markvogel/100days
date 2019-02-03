# Programming in C++ second edition page 202 - ch 5 problem 1


def phone_digit(a: str = None):
    phone_digits = {'a': 2, 'b': 2, 'c': 2,
                    'd': 3, 'e': 3, 'f': 3,
                    'g': 4, 'h': 4, 'i': 4,
                    'j': 5, 'k': 5, 'l': 5,
                    'm': 6, 'n': 6, 'o': 6,
                    'p': 7, 'q': 7, 'r': 7, 's': 7,
                    't': 8, 'u': 8, 'v': 8,
                    'w': 9, 'x': 9, 'y': 9, 'z': 9}
    if a in phone_digits:
        return phone_digits.get(a)


if __name__ == '__main__':
    word = input("Please enter a word and I will return the equivalent phone digits:")
    word = ''.join([str(phone_digit(i)) for i in word.lower()])
    print(word)
