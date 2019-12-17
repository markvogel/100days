class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(x=1, y=2, z=3)
print(my_point)

my_file = open("output.txt", "r+")

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!

for i in my_list:
    my_file.write(str(i) + "\n")
my_file.close()

my_file = open("output.txt", "r")
print(my_file.read())
my_file.close()

my_file = open("text.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()
