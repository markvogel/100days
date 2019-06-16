# https://www.py4e.com/html3/06-strings
def c6_e1():
    str1 = "hello"

    index = 0
    while index < (len(str1) - 1):
        if abs(index) == len(str1):
            break
        print(str1[index - 1])
        index = index - 1


if __name__ == '__main__':
    c6_e1()
