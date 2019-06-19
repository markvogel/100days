# https://www.py4e.com/html3/07-files


# exercise 1
def open_file():
    f_name = input("Enter a file name: ")
    if f_name.lower() == "na na boo boo":
        egg()
    try:
        f = open(f_name)
        return f
    except FileNotFoundError:
        print("File can't be opened: ", f_name)
        exit()


# exercise 3
def egg():
    print("na na boo boo".upper() + " TO YOU - You have been punk'd")
    exit()


def upper_print(f):
    for line in f:
        print(line.upper())


# exercise 2
def find_dspam(f):
    spam = []
    for line in f:
        if line.startswith("X-DSPAM-Confidence"):
            current_line = line.split(":")
            spam.append(float(current_line[1]))
    avg_spam = sum(spam) / len(spam)
    print(f"Average spam confidence: {avg_spam}")


if __name__ == '__main__':
    # upper_print(open_file())
    find_dspam(open_file())
