my_dict = {"a": "alpha",
           "b": "bravo",
           "c": "charlie",
           "d": "delta"}

print(my_dict.items())
print(my_dict.keys(), my_dict.values())

for i in my_dict.items():
    print(i, end=" ")

for key, value in my_dict.items():
    print(key, value)

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

print(even_squares)

cubes_by_four = [i ** 3 for i in range(1, 11) if (i ** 3) % 4 == 0]

print(cubes_by_four)

my_list = range(1, 11)

print(my_list[::2])
backwards = my_list[::-1]

to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]

languages = ["HTML", "JavaScript", "Python", "Ruby"]

print(filter(lambda x: x.startswith("Py"), languages))

squares = [x ** 2 for x in range(1, 11)]
print(filter(lambda x: 30 <= x <= 70, squares))
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())

threes_and_fives = [i for i in range(1, 16) if i % 3 == 0 or i % 5 == 0]
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != 'X', garbled)
print(message)
