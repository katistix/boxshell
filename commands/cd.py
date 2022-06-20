import os
from colorama import Fore
from colorama import Style

def cd(ARGS):
    path = ARGS[0] if len(ARGS) > 0 else os.getcwd()
    try:
        os.chdir(path)
        print(f'{Fore.LIGHTYELLOW_EX}{os.getcwd()}{Style.RESET_ALL}')
    except FileNotFoundError:
        print(f'{Fore.LIGHTRED_EX}cd: {path}: No such file or directory{Style.RESET_ALL}')
        return