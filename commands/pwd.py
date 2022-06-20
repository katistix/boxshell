import os
from colorama import Fore
from colorama import Style

def pwd():
    print(f'{Fore.LIGHTYELLOW_EX}{os.getcwd()}{Style.RESET_ALL}')