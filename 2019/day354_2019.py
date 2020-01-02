with open("text.txt", "w") as my_file:
    my_file.write("hello there")

if not my_file.closed:
    my_file.close()

print(my_file.closed)
