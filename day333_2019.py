grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for i in grades_input:
        print(i)


def grades_sum(scores):
    return sum(scores)


def grades_average(grades_input):
    return (grades_sum(grades_input)) / float(len(grades_input))


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    return variance / len(scores)


if __name__ == '__main__':
    print_grades(sorted(grades, reverse=True))
    print(grades_sum(grades))
    print(grades_average(grades))
    print(grades_variance(grades))
