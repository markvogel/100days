# Python interview question compliments of https://www.interviewcake.com/python-interview-questions
# output should be as follows:
# "slice starting 3 days ago: [108.67, 109.86]"
# "slice starting 2 days ago: [109.86, 110.15]"

list_balances = [107.92, 108.67, 109.86, 110.15]
list_balances2 = [107.92, 108.67, 109.86, 110.15, 111.11, 112.32, 113.01]


# given example
def show_balances(daily_balances):
    # do not include -1 because that slice will only have 1 balance, yesterday
    for day in range(-3, -1):
        balance_slice = daily_balances[day: day + 2]

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(day), balance_slice))


# my solution
def show_balances_me(daily_balances):
    total_balances = len(daily_balances)
    for day in range(total_balances - 3, total_balances - 1):
        balance_slice = daily_balances[day: day + 2]
        print(f"slice starting {total_balances - day} days ago: {balance_slice}")
    return balance_slice


# given solution
def show_balances_solution(daily_balances):
    num_balances = len(daily_balances)

    # still avoid slice that just has yesterday
    for day in range(num_balances - 3, num_balances - 1):
        balance_slice = daily_balances[day: day + 2]

        # need to calculate how many days ago
        days_ago = num_balances - day
        print("slice starting %d days ago: %s" % (abs(days_ago), balance_slice))


def test_answer():
    assert show_balances([109.86, 110.15]) == [109.86, 110.15]


if __name__ == '__main__':
    show_balances_me(list_balances)
