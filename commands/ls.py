import os
from colorama import Fore
from colorama import Style

def ls(ARGS):
    path = ARGS[0] if len(ARGS) > 0 else os.getcwd()
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f'{Fore.LIGHTRED_EX}ls: {path}: No such file or directory{Style.RESET_ALL}')
        return
    
    for file in files:
        isDir = os.path.isdir(f'{path}/{file}')
        if ' ' in file:
            file = f"'{file}'"
        if isDir:
            print(file, end=' ')
        else:
            print(f'{Fore.LIGHTCYAN_EX}{file}{Style.RESET_ALL}', end=' ')
    print()