import os
import time
import pyfiglet
from colorama import Fore
from subprocess import call

MSG = 'Happy New Year 2020'
FRONT = 'slant'


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls', shell=True)


def print_nye_to_console():
    f = pyfiglet.Figlet(font=FRONT)
    clear()
    for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW] * 10 + [Fore.WHITE]:
        print(col + f.renderText(MSG))
        time.sleep(0.05)
        clear()


if __name__ == '__main__':
    print_nye_to_console()
