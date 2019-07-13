import os

os.chdir(r'c:\test')

for c, i in enumerate(os.listdir()):
    os.rename(i, f"test_file{c}")
