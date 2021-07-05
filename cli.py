
"""
CLI Interface Template
Author: Hussein Esmail
Date Created: 2020 07 22
Date Updated: 2020 07 22
Description: This program is a skeleton template for an infinite-input program
"""

import sys

def main():
    # VARIABLES
    user_args = sys.argv
    str_invalid = "Invalid command!"
    exit_commands = ["exit", "exit()", "e", "quit", "quit()", "q"] # If the user types any of these, quit the program
    
    # Startup code goes here
    
    while True: # Keep going until the user quits the program
        if user_args[0] in exit_commands and len(user_args) == 1:
            sys.exit() # Exit the program
        elif user_args[0] == "help" and len(user_args) == 1:
            print("This would be the help command")
            # More commands would be each elif statement.
        else:
            if len(user_args) and user_args[0] == "": # If the user just pressed ENTER
                pass
            else:
                print(str_invalid)
            
if __name__ == "__main__":
    main()
