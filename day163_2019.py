import statistics


# https://www.py4e.com/html3/03-conditional
def c3_e3():
    min_grade, max_grade = 0.0, 1.0
    try:
        grade = float(input(f"Please enter a score between {min_grade} and {max_grade}: "))
        print(calc_grade(grade))
    except ValueError:
        print("Bad score")


def calc_grade(g: float):
    g = int(g * 10)
    if g < 6:
        return "F"
    grade_table = {9: "A", 8: "B", 7: "C", 6: "D"}
    return grade_table.get(g)


# https://www.py4e.com/html3/04-functions
def compute_pay(hours, rate):
    try:
        hours = float(hours)
    except ValueError:
        print("Error, non-numeric input")
        exit()
    try:
        rate = float(rate)
    except ValueError:
        print("Error, non-numeric input")
        exit()
    if hours > 40:
        overtime_hours = hours - 40
        hours = hours - overtime_hours
        pay = (hours * rate) + (overtime_hours * (rate * 1.5))
    else:
        pay = (hours * rate)
    pay = round(pay, 2)
    print(f"Hours: {hours}")
    print(f"Rate: {rate}")
    print(f"Pay: {pay}")


def read_numbers():
    num_list = []
    num = None
    while num != "done":
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            num = float(num)
            num_list.append(num)
        except ValueError:
            print("Invalid input")
            print(num_list)
            read_numbers()
    return num_list


def c5_e1():
    a = read_numbers()
    print(sum(a), len(a), sum(a) / len(a))


def c5_e2():
    a = read_numbers()
    print(max(a), min(a))


if __name__ == '__main__':
    # c = "y"
    # while c != "n":
    #     c3_e3()
    #     c = input("Would you like to continue? (y)es or (n)o?")
    # compute_pay(45, 10)
    c5_e1()
    c5_e2()
