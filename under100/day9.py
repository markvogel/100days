# simple automation of opening an application, and sending some various keystrokes

import pyautogui as p
import subprocess
import time

# if pyautogui.size() == (1920, 1080):
subprocess.Popen(r'C:\WINDOWS\system32\notepad.exe')
time.sleep(1)
p.click(1007, 637)
p.hotkey('win', 'right')
# p.press('enter')
p.click(1338, 94)
p.click(1281, 585)
p.typewrite('Hello World!')
p.click(1565, 614)
