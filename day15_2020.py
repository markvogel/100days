# https://www.w3resource.com/python-exercises/python-basic-exercises.php

"""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are

"""

sample = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"


def twinkle():
    print(sample[:31])
    print(f'\t{sample[31:57]}')
    print(f'\t\t{sample[57:85]}')
    print(f'\t\t{sample[85:112]}')
    print(sample[112:143])
    print(f'\t{sample[143:]}')


if __name__ == '__main__':
    twinkle()