def greeting():
    user = input("Please enter your name: ")
    print(f"Hello, {user}!")


def wage():
    hours = float(input(("Please enter the total number of hours: ")))
    rate = float(input("Please enter the rate per hour: "))
    pay = hours * rate
    pay = round(pay, 2)

    print(f"Pay: {pay}")


if __name__ == '__main__':
    # greeting()
    wage()
