# https://www.py4e.com/html3/06-strings
# exercise 2


def count2(word='banana'):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)


def c6e5(str1='X-DSPAM-Confidence:0.8475'):
    a = str1.find(':')
    num = float(str1[a + 1:])
    print(num)


if __name__ == '__main__':
    count2()
    # exercise 4
    print('banana'.count('a'))
    c6e5()
