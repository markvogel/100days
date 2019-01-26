"""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond
 in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are"""

# * https://www.reddit.com/r/dailyprogrammer/
# * https://www.practicepython.org/
# * http://www.100daysofcode.com/
# * https://www.w3resource.com/python-exercises/
sample_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond" \
                " in the sky. Twinkle, twinkle, little star, How I wonder what you are"

print(sample_string[:30] + '\n' + '\t' + sample_string[30:58])
print('\t\t' + sample_string[58:86])
print('\t\t' + sample_string[86:113])
print(sample_string[113:143] + '\n' + '\t' + sample_string[143:171])
