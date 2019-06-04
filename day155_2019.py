import os
import ipaddress


def ping_host(host):
    response = os.system(f' ping -n 1 {host} | find "Reply" > nul')
    if response == 0:
        ping_status = "online"
    else:
        ping_status = "offline"
    return ping_status


def create_ips(str1):
    return [str1 + str(ii) for ii in range(1, 255)]


if __name__ == '__main__':

    a = ipaddress.IPv4Network("10.0.0.0/24")
    for i in a:
        print(i)
    test = []
    online = []
    for i in test:
        if ping_host(i) == "online":
            online.append(i)
    print(online)
