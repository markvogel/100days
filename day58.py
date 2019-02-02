import datetime

day_of_the_week = (datetime.datetime.today().strftime("%A"))


def calc_day_of_week():
    julian_day = get_julian_day()
    day_of_week = (int(julian_day) + 1) % 7
    return day_of_week


def get_julian_day():
    return input("Enter a Julian day number:\n")


def find_day(day_num: int):
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    return days.get(day_num)


def calc_easter(year_num: int):
    a = year_num % 19
    b = year_num % 4
    c = year_num % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    f = (22 + d + e)
    if f > 31:
        f -= 31
        month = 'April'
    else:
        month = 'March'

    return f"Easter Sunday is {month} {f}, {year_num}"


if __name__ == '__main__':
    # print(find_day(calc_day_of_week()))
    print(calc_easter(2048))
