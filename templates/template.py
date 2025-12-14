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
PROGRAM_NAME = "FILL IN PROGRAM NAME HERE" # TODO
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


def yes_or_no(str_ask):
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

def parse_args(argv=None):
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description="Short description of your command-line tool." # TODO
    )

    # Positional arguments
    parser.add_argument(
        "input",
        nargs="?",
        help="Input file or value"
    )

    # Optional arguments
    parser.add_argument(
        "-o", "--output",
        help="Output file path"
    )

    parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    # Version flag
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Display version number"
    )

    return parser.parse_args(argv)



def main(argv=None):
    args = parse_args(argv)
    
    if args.verbose:
        # A better solution over a 'bool_prints' variable
        print("Verbose mode enabled", file=sys.stderr)

    if args.input:
        if args.verbose:
            print(f"Input: {args.input}", file=sys.stderr)
    else:
        print("No input provided", file=sys.stderr)

    if args.output and args.verbose:
        print(f"Output will be written to: {args.output}", file=sys.stderr)

    # CODE HERE
    # result = do_work(args.input)
    # NOTE: variables with a single underscore as its first character are not
    # copied over if this program is imported into something else. Ex. _array2
    # vs array2

    print(args)

    return 0 # Completed successfully


if __name__ == "__main__":
    sys.exit(main())
    # Exit the program, returning the return code of main() - can be 1, 0, etc
