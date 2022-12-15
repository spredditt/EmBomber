# Author: spredditt

import os

try:
    os.system('chmod +x EmBomber.py')
    os.system('cp EmBomber.py ~bin/mail-bomb')
except IOError as e:
    print("Run as root")