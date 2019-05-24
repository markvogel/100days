from under100.day65 import test


def test_suite():
    chatroom_status([])  # "no one online"

    chatroom_status(["paRIE_to"])  # "parIE_to online"

    chatroom_status(["s234f", "mailbox2"])  # "s234f and mailbox2 online"

    chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
    # "pap_ier44, townieBOY and 4 more online"


# https://edabit.com/challenge/PwGFjiSG3kXzp8rjw
def chatroom_status(users):
    if len(users) == 0:
        print("no one online")
    if len(users) == 1:
        print(f"{users[0]} online")
    if len(users) == 2:
        print(f"{users[0]} and {users[1]} online")
    if len(users) > 2:
        print(f"{users[0]}, {users[1]} and {len(users) - 2} more online")


if __name__ == '__main__':
    test_suite()
