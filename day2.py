# this will get the mac address of a target machine and send it a magic packet to get it to wakeup
from wakeonlan import send_magic_packet
from getmac import get_mac_address
import myconstants


def wake_computer(host):
    send_magic_packet(get_mac_address(hostname=host))


if __name__ == '__main__':
    wake_computer(myconstants.test)
