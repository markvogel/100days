import os
from os import listdir


def powershell_command(command):
    os.system(f'powershell {command}')


def get_users(location):
    return listdir(f"//{location}fps01/Users")


def app(loc):
    users = get_users(loc)
    print(loc)
    for user in users:
        print(user)
        powershell_command(f"Get-ADUser -Identity {user} -Properties UserPrincipalName")


def app2():
    with open("day98_2020_output.txt") as f:
        dlist = f.readlines()
    for i in dlist:
        if i.startswith("UserPrincipalName"):
            print(i.split()[-1])


if __name__ == '__main__':
    app("")
    # app2()
