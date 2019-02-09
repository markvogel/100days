from bokeh.plotting import figure, show, output_file
from day63 import months, counts


def test():
    output_file("plot.html")

    x = [10, 20, 30]
    y = [4, 5, 6]

    p = figure()

    p.vbar(x=x, top=y, width=0.5)

    show(p)


def test2():
    output_file("plot.html")
    # x_categories = ["a", "b", "c", "d", "e"]
    # x = ["a", "d", "e"]
    # y = [4, 5, 6]
    x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                    "November", "December"]
    x = months
    y = counts
    p = figure(x_range=x_categories, x_axis_label="birthdays")
    p.vbar(x=x, top=y, width=0.5)

    show(p)


if __name__ == '__main__':
    test2()
