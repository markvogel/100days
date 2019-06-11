def greeting():
    user = input("Please enter your name: ")
    print(f"Hello, {user}!")


def wage():
    hours = input("Please enter the total number of hours: ")
    rate = input("Please enter the rate per hour: ")
    pay = int(hours) * int(rate)
    pay = round(pay, 2)

    print(f"Pay: {pay}")


if __name__ == '__main__':
    # greeting()
    wage()
