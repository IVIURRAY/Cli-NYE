import os
import time
import pyfiglet
from colorama import Fore
from subprocess import call


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')


f = pyfiglet.Figlet(font='slant')

for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.BLACK] * 2:
    print(col + f.renderText('Happy New Year 2020'))
    time.sleep(0.5)
    clear()

print(Fore.WHITE + f.renderText('Happy New Year 2020'))
