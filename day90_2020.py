import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import pyping


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


if __name__ == '__main__':
    with open("devices.txt") as f:
        dlist = f.readlines()
    # for i in dlist:
    #     i = (i.strip())
    #     print(ping(i))
    # with open("devices2.txt", "w") as o:
    #     pass

    r = pyping.ping(dlist[0].strip())
