print(bin(0b1110 & 0b101))
print(bin(0b1110 | 0b101))
print(bin(0b1110 ^ 0b101))


def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"
