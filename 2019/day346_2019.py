class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return (self.angle1 + self.angle2 + self.angle3) == 180


my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1, self.angle2, self.angle3 = self.angle, self.angle, self.angle


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type


my_car = ElectricCar("leaf", "green", 123, "molten salt")
