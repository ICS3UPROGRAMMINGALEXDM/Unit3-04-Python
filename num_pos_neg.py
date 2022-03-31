#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Tells user if their number is positive negative or 0

import colorama
from colorama import Fore, Back, Style


def main():
    # Get number from user
    num = int(input(Fore.WHITE + Style.BRIGHT + "Enter a number: "))

    # If statement that decides what to do with the number
    if num > 0:
        print(Fore.MAGENTA + "Your number is positive")
    elif num < 0:
        print(Fore.CYAN + "Your number is negative")
    else:
        print(Fore.YELLOW + "Your number is 0")


if __name__ == "__main__":
    main()
