"""
Python Password Generator
Hussein Esmail
Created: 2020 09 06
Updated: 2020 12 14
Description: This program generates a random password that can be used
    when creating internet accounts. If a number is typed along
    with the 'python3 password_generator.py', it will make a password of
    that length. For example: 'python3 password_generator.py 10'.
"""

import random   # Used to randomize the characters
import string   # Used to get the alphabet and numbers as str
import sys      # Used to exit the program
import pyperclip # Used to copy the password for the user

def main():
    if len(sys.argv) > 1: # If there were arguments passed through
        if sys.argv[-1].lower() == "help": # Help command
            print("This program generates a random password that can be used" + \
                "\n\twhen creating internet accounts. If a number is typed along " + \
                "\n\twith the 'python3 password_generator.py', it will make a password of " + \
                "\n\tthat length. For example: 'python3 password_generator.py 10'. ")
            print("For some reason, this program cannot generate a password longer than 75 characters.")
            sys.exit() # Exit the program, because if the help message is displayed, don't run the password generator part.
        else: # If the last command is not "help"
            length = int(sys.argv[1])
    else:
        length = 16 # How long you want the password to be in characters
    lower = string.ascii_lowercase # Lowercase alphabet as string
    upper = string.ascii_uppercase # Uppercase aplhabet as string
    numbers = string.digits # 0-9 as string
    symbols = "[]{}()*;/,._-" # Allowed special symbols
    # print("For more info about this program, type 'help' as the last argument")
    password = "".join(random.sample(lower + upper + numbers + symbols, length))
    pyperclip.copy(password)
    print(password + "\t - Copied") # Print the randomized password
    sys.exit()
    
if __name__ == "__main__":
    main()