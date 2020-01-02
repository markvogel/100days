one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print(bin(1))
print(oct(1))
print(hex(1))
for i in range(2, 6):
    print(bin(i))
print([bin(x) for x in range(2, 6)])

print(int("1", 2))
print(int("10", 2))
print(int("111", 2))
print(int("0b100", 2))
print(int(bin(5), 2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))
