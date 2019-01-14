# This is intended to shutdown computers remotely in a Windows domain environment

import os
import myconstants


def powershell_command(command):
    os.system(f'powershell {command}')


def stop_computers(computer: str = "Error: No host entered"):
    try:
        powershell_command("Stop-Computer -Force -ComputerName " + computer)
        print('shutdown ' + computer)
    except:
        print("Could not shutdown " + computer)


if __name__ == '__main__':
    stop_computers(myconstants.test_host)
