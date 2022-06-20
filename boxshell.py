import sys
import os
from colorama import Fore
from colorama import Style
from pathlib import Path

# Commands
import commands.ls as LS
import commands.cd as CD
import commands.pwd as PWD
import commands.help as HELP


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        cmdline = input(f'{Fore.LIGHTYELLOW_EX}❯{Style.RESET_ALL} ')
        CMD = cmdline.split(' ')[0]
        ARGS = cmdline.split(' ')[1:]
        if CMD.isspace() or CMD == '':
            continue
        elif CMD == 'help':
            HELP.help()
        elif CMD == 'ls':
            LS.ls(ARGS)
        elif CMD == 'cd':
            CD.cd(ARGS)
        elif CMD == 'pwd' or CMD == 'cwd':
            PWD.pwd()
        elif CMD == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit(0)

        elif CMD == 'clear' or CMD == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f'⚠️ Command not found, using system shell\n')
            os.system(cmdline)