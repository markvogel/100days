from under100.day65 import test


# https://www.py4e.com/html3/02-variables
def c2_exercise5():
    c_temp = float(input("Please enter a temperature in Celsius: "))
    f_temp = c_temp * 9 / 5 + 32
    print(f"Celsius temperature of {c_temp} is equal to Fahrenheit temperature of {f_temp}")


# https://www.py4e.com/html3/03-conditional
def c3_e1():
    hours = float(input(("Please enter the total number of hours: ")))
    rate = float(input("Please enter the rate per hour: "))
    if hours > 40:
        overtime_hours = hours - 40
        hours = hours - overtime_hours
        pay = (hours * rate) + (overtime_hours * (rate * 1.5))
    else:
        pay = (hours * rate)
    pay = round(pay, 2)
    print(f"Pay: {pay}")


# https://www.py4e.com/html3/03-conditional
def c3_e2():
    hours, rate = 0, 0
    try:
        hours = float(input(("Please enter the total number of hours: ")))
    except ValueError:
        print("Error, please enter numeric input")
        exit()
    try:
        rate = float(input("Please enter the rate per hour: "))
    except ValueError:
        print("Error, please enter numeric input")
        exit()
    if hours > 40:
        overtime_hours = hours - 40
        hours = hours - overtime_hours
        pay = (hours * rate) + (overtime_hours * (rate * 1.5))
    else:
        pay = (hours * rate)
    pay = round(pay, 2)
    print(f"Pay: {pay}")


if __name__ == '__main__':
    c3_e2()
