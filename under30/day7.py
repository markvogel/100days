# get a list of computers from active directory, if the host is online, copy files to the hard drive across the network

from under30.day1 import copy_network_files
from under30 import day5, day4
import myconstants


def sync_pcs():
    computer_hostnames = day4.get_pcs()
    for hostname in computer_hostnames:
        if day5.ping_host(hostname) == 'online':
            try:
                copy_network_files(hostname, myconstants.a, myconstants.aa)
                copy_network_files(hostname, myconstants.b, myconstants.bb)
                copy_network_files(hostname, myconstants.c, myconstants.cc)
                # print(f'copied files to {hostname}')
            except:
                print(f'files not copied to {hostname}')
                continue
        else:
            print(f'{hostname} offline')


if __name__ == '__main__':
    sync_pcs()
