import os
import time
import pyfiglet
from colorama import Fore
from subprocess import call

msg = 'Happy New Year 2020'

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')


f = pyfiglet.Figlet(font='slant')

clear()
for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW] * 2 + [Fore.WHITE]:
    print(col + f.renderText(msg))
    time.sleep(0.5)
    clear()
