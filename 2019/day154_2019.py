#!/usr/bin/env python
import nmap  # import nmap.py module

nm = nmap.PortScanner()  # instantiate nmap.PortScanner object

if __name__ == '__main__':
    nm.scan(hosts='127.0.0.1')
    print(nm.command_line())
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
