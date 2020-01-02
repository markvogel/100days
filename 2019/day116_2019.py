from under100.day65 import test
from datetime import datetime

day_of_year = datetime.now().timetuple().tm_yday


# https://edabit.com/challenge/2yHQwkecEHZBfHcmN
def progress_days(lst):
    progress = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            progress += 1
    return progress


def test_suite():
    test(progress_days([3, 4, 1, 2]) == 2)
    test(progress_days([10, 11, 12, 9, 10]) == 3)
    test(progress_days([6, 5, 4, 3, 2, 9]) == 1)
    test(progress_days([9, 9]) == 0)
    test(progress_days([12, 11, 10, 12, 11, 13]) == 2)


if __name__ == '__main__':
    test_suite()
    # print(day_of_year)
