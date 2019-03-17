# program to see if a host is active on the network
import os
import myconstants


def ping_host(host):
    response = os.system(f' ping -n 1 {host} | find "Reply" > nul')
    if response == 0:
        ping_status = "online"
    else:
        ping_status = "offline"
    return ping_status


if __name__ == '__main__':
    print(ping_host(myconstants.test_host2))
