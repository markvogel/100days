from day65 import test
import turtle  # Allows us to use turtles


def move_alex(turn, steps):
    alex.left(turn)
    alex.forward(steps)


def list_move_alex(a_list):
    for i in a_list:
        move_alex(i[0], i[1])


def list_move_alex2(b_list):
    for i in b_list:
        list_move_alex(i)


def test_suite():
    pass


if __name__ == '__main__':
    wn = turtle.Screen()  # Creates a playground for turtles
    # test_suite()
    alex = turtle.Turtle()  # Create a turtle, assign to alex
    experimental = [(135, 141.42), (-135, 100), (-135, 141.42), (-135, 100), (-45, 70.71), (-90, 70.71), (-45, 100),
                    (-90, 100)]
    list_move_alex(experimental)
    
    wn.mainloop()  # Wait for user to close window
