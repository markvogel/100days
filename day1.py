# This will copy all files in a folder to an admin share on a network computer in a domain environment
import os
import shutil
import myconstants


def copy_public_desktop(target, source=myconstants.PUBLIC_DESKTOP):
    src_files = os.listdir(source)
    for file_name in src_files:
        full_file_name = os.path.join(source, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, f"\\\\{target}\\C$\\Users\\Public\\Desktop\\")


if __name__ == '__main__':
    copy_public_desktop(myconstants.test)
