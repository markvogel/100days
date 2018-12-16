# number guessing game to play with children
import random
import os

number = random.randint(1, 20)
guess = 0
print("I'm thinking of a number between 1 and 20 please guess what it is. ")
response = {"correct": "You guessed my number, great job!",
            "low": "The number that you guessed is too low, try again",
            "high": "The number that you guessed is too high, try again",
            "sorry": "You ran out of guesses, too bad, sorry!"}
for i in range(5):
    guess_num = i + 1
    if i < 4:
        print("You have " + str(6 - guess_num) + " guesses left: ", end='')
    if guess_num == 5:
        print("this is your last guess, choose wisely!")
    guess = int(input())
    if guess == number:
        print(response.get("correct"))
        os.system(r'C:\Windows\media\tada.wav')
        quit()
    if guess < number:
        print(response.get("low"))
    if guess > number:
        print(response.get("high"))
print(response.get("sorry"))
