'''
[FILENAME]
[AUTHOR]
Created: [DATE]
Updated: [DATE]
Description: [DESCRIPTION] # TODO
'''

# This part is used for https://github.com/hussein-esmail7/template-maker
# templateDescription: Python Programming Document Without Config

import os
import sys
import argparse

# ========= VARIABLES ===========
PROGRAM_NAME = "FILL IN PROGRAM NAME HERE" # TODO: Program name here
__version__ = "0.1.0"

# ========= COLOR CODES =========
color_end               = '\033[0m'
color_darkgrey          = '\033[90m'
color_red               = '\033[91m'
color_green             = '\033[92m'
color_yellow            = '\033[93m'
color_blue              = '\033[94m'
color_pink              = '\033[95m'
color_cyan              = '\033[96m'
color_white             = '\033[97m'
color_grey              = '\033[98m'

# ========= COLORED STRINGS =========
str_prefix_q            = f"[{color_pink}Q{color_end}]\t "
str_prefix_y_n          = f"[{color_pink}y/n{color_end}]"
str_prefix_err          = f"[{color_red}ERROR{color_end}]\t "
str_prefix_done         = f"[{color_green}DONE{color_end}]\t "
str_prefix_info         = f"[{color_cyan}INFO{color_end}]\t "
error_neither_y_n = f"{str_prefix_err} Please type 'yes' or 'no'"


def yes_or_no(str_ask: str):
    while True:
        y_n = input(f"{str_prefix_q} {str_prefix_y_n} {str_ask}").lower()
        if y_n[0] == "y":
            return True
        elif y_n[0] == "n":
            return False
        if y_n[0] == "q":
            sys.exit()
        else:
            print(f"{str_prefix_err} {error_neither_y_n}")

def parse_args(argv):
    # TODO: Specify the type input to be the same as the type of sys.argv, then remove "type: ignore" comment associated to other instances of this function
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description="Short description of your command-line tool." # TODO
    )

    # Positional arguments
    parser.add_argument(
        "input",
        nargs="?", # If "None" or "?", each character of the argument string will be appended to the list
        # default="str" is also doable, but:
        # 1. the presence of it means that input is also accepted.
        # 2. If you want the no input error to run, do not put the line
        help="Input file or value"
    )

    # If there is an output file, list the path you want it to be
    parser.add_argument(
        "-o", "--output",
        # Since no 'action' parameter set, string required
        help="Output file path. Ex: -o=\"path\""
    )

    # Also used for debugging
    parser.add_argument(
        "-V", "--verbose",
        action="store_true", # Just store true if present, string not required afterwards
        help="Enable verbose output"
    )

    # Version flag
    parser.add_argument(
        # NOTE: Program also exits when this argument is invoked
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Display version number"
    )

    return parser.parse_args(argv)



def main():

    args = parse_args(sys.argv) # type: ignore
    
    if args.verbose:
        # A better solution over a 'bool_prints' variable
        print("Verbose mode enabled", file=sys.stderr)

    if args.input:
        # There is input present
        if args.verbose:
            print(f"Input: {args.input}", file=sys.stderr)
    else:
        print("No input provided", file=sys.stderr)
        # return -1 # Exit if input is required each time

    if args.output and args.verbose:
        # TODO: Make args.output do something
        print(f"Output will be written to: {args.output}", file=sys.stderr)

    if args.output:
        # Convert path to a usable format
        if args.output.contains("~"):
            # Expand ~ to home path
            args.output = os.path.expanduser(args.output)
        # If a file is required:
        if not os.path.isfile(args.output):
            # At this point we know a file was not provided
            if os.path.isdir(args.output):
                # At this point, we know they provided a folder
                # NOTE: os.path.isdir only passes for existing folders
                print("Please provide a file path, not a directory", file=sys.stderr)
            elif args.output.endswith("/"):
                # User is trying to provide a folder that does not exist yet, or
                # an incorrect path/typo (since it failed os.path.isfile and
                # os.path.isdir)
                print("Directory does not exist", file=sys.stderr)
                return -1 # Exit, since given an incorrect input
            else:
                # If the program is able to work with the folder, and name the file itself
                if not args.output.endswith("/"):
                    # It can pass the check of it being a folder 
                    args.output = args.output + "/"



        

    # if args.verbose:
    #     # Debug print statement
    #     print(f"{str_prefix_info} INFORMATIVE PRINT STATEMENT TEMPLATE")


    # CODE HERE
    # result = do_work(args.input)
    # NOTE: variables with a single underscore as its first character are not
    # copied over if this program is imported into something else. Ex. _array2
    # vs array2

    print(args) # returns Namespace type

    return 0 # Completed successfully


if __name__ == "__main__":
    sys.exit(main())
    # Exit the program, returning the return code of main() - can be 1, 0, etc
