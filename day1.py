# This will copy all files in a folder to an admin share on a network computer in a domain environment
import os
import shutil
import myconstants


def copy_network_files(host: str, source: str, destination: str):
    destination = f'\\\\{host}\\C$\\{destination}'
    src_files = os.listdir(source)
    if not os.path.exists(destination):
        os.mkdir(destination)
    for file_name in src_files:
        full_file_name = os.path.join(source, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination)


if __name__ == '__main__':
    pass
