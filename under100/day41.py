# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
import statistics


def check_guess():
    return input('Please tell me whether my guess is too high, too low, or the number ')


def print_guess(num1: int):
    print(f'I guess that your number is {num1}')


if __name__ == '__main__':
    guess = 50
    is_it_correct = ''
    num_guesses = 0
    while is_it_correct != 'too high' or 'too low' or 'the number':
        num_guesses += 1
        print_guess(guess)
        is_it_correct = check_guess()
        if is_it_correct == 'the number':
            print(f"Awesome, it took me {num_guesses} guess(es) to guess your number")
            break
        if is_it_correct == 'too high':
            guess = int(statistics.median(range(1, guess)))
        if is_it_correct == 'too low':
            guess = int(statistics.median(range(1, guess))) + 50
