# similar to day3, this program runs a powershell command, this time using subprocess instead of os.system
# this program is intended to find the install date of a machine on the network

import subprocess


def get_install_date(hostname: str = 'localhost'):
    return powershell_command(f'(Get-WmiObject Win32_OperatingSystem -ComputerName {hostname}).InstallDate')


def powershell_command(command: str = 'echo no command entered'):
    return subprocess.run(f'powershell {command}', stdout=subprocess.PIPE)


def parse_install_date(install_date: str = '  19700101'):
    year = install_date[2:6]
    month = install_date[6:8]
    day = install_date[8:10]
    date = f'{month}/{day}/{year}'
    return date


if __name__ == '__main__':
    host_install_date = str((get_install_date()).stdout)
    print(parse_install_date(host_install_date))
