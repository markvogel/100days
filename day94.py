from day65 import test


# how to think like a computer scientist: learning with Python 3 19.6

def readposint():
    user_input = input("Please enter a positive integer: ")
    try:
        int_input = int(user_input)
        if int_input >= 0:
            print(f"Great! You entered '{int_input}', thank you for entering a positive integer.")
        else:
            print("You didn't enter a positive integer, please enter a positive integer")

    except ValueError:
        value_error = ValueError(f"You entered '{user_input}' which is not a positive integer.")
        raise value_error
    except EOFError:
        print("You didn't enter a value, please enter a positive integer.")


def test_suite():
    pass


if __name__ == '__main__':
    test_suite()
    readposint()
