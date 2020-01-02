from under100.day65 import test

import turtle

turtle.setup(400, 500)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Handling keypresses!")  # Change the window title
wn.bgcolor("lightgreen")  # Set the background color
tess = turtle.Turtle()  # Create our favorite turtle


# The next four functions are our "event handlers".
def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()  # Close down the turtle window


def h5():
    tess.color('red')


def h6():
    tess.color('green')


def h7():
    tess.color('blue')


def h8():
    a = tess.pensize()
    if a >= 20:
        return
    a += 1
    tess.pensize(a)


def h9():
    a = tess.pensize()
    if a == 1:
        return
    a -= 1
    tess.pensize(a)


def tuple_test(a, b):
    return b, a


def test_suite():
    test(tuple_test(1, 2) == (2, 1))
    test(tuple_test(100, 200) == (200, 100))
    test(tuple_test("abc", 39) == (39, "abc"))


if __name__ == '__main__':
    # test_suite()
    # These lines "wire up" keypresses to the handlers we've defined.
    wn.onkey(h1, "Up")
    wn.onkey(h2, "Left")
    wn.onkey(h3, "Right")
    wn.onkey(h4, "q")
    wn.onkey(h5, "r")
    wn.onkey(h6, "g")
    wn.onkey(h7, "b")
    wn.onkey(h8, "+")
    wn.onkey(h9, "-")

    # Now we need to tell the window to start listening for events,
    # If any of the keys that we're monitoring is pressed, its
    # handler will be called.
    wn.listen()
    wn.mainloop()
