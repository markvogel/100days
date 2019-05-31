# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
def list_comprehensions(lst):
    return [i for i in lst if not i % 2]


# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
def rock_paper_scissors():
    p1 = player_input()
    p2 = player_input()
    print(winner(p1, p2))
    play_again = input("Would you like to play again? (y) or (n): ")
    while play_again != "n":
        rock_paper_scissors()


def winner(str1, str2):
    win = {"player1": [["rock", "scissors"], ["scissors", "paper"], ["paper", "rock"]]}
    if str1 == str2:
        return "It's a tie!"
    if [str1, str2] in win.get("player1"):
        return "Player 1 wins!"
    return "Player 2 wins!"


def player_input():
    p_input = ""
    while p_input != "rock" and p_input != "paper" and p_input != "scissors":
        p_input = input("Please enter rock, paper or scissors: ")
    return p_input


if __name__ == '__main__':
    # a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # print(list_comprehensions(a))
    rock_paper_scissors()
