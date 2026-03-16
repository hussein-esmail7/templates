'''
[FILENAME]
[AUTHOR]
Created: [DATE]
Updated: [DATE]
Description: [DESCRIPTION] # TODO
'''

# This part is used for https://github.com/hussein-esmail7/template-maker
# templateDescription: Python RSS Scraper to RSS Feed

import os
import sys
import datetime
import urllib.request # Used to test internet connection
import argparse
import to_rss # TODO: ~/git/rss-parsers/src/to_rss.py library needed.
# https://github.com/hussein-esmail7/rss-parsers/blob/main/src/to_rss.py
from email.utils import format_datetime # Convert datetime object to RFC822, which RSS 2.0 requires

# ========= VARIABLES ===========
PROGRAM_NAME = "RSS - FILL IN PROGRAM NAME HERE" # TODO: Program name here
__version__ = "0.1.0"
# NOTE: Uncomment if using Selenium. Delete if not.
# bool_run_in_background  = True # Hide selenium Chrome window
bool_output_to_json = False
rss_title = "TITLE" # TODO: RSS Feed title here, or set to PROGRAM_NAME
rss_subtitle = "DESC" # TODO RSS Single line description here
rss_author = "" # TODO: RSS author of the RSS post
rss_path = path + "FILENAME.xml" # TODO
target_url = "https://google.com" # TODO: Target URL to make feed from

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
str_prefix_info_red     = f"[{color_red}INFO{color_end}]\t "
error_neither_y_n = f"{str_prefix_err} Please type 'yes' or 'no'"

def is_internet_connected():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def erase_blank_lines(list):
    is_str = type(list) is str # How to return variable in the type it was
    if is_str:
        list = list.split("\n")
    for item in list:
        if item.strip() == "":
            del item
    if is_str:
        return "\n".join(list)
    return list

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

def parse_args(argv=None):
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



def main(argv=None):
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


    # RSS parser code begins here
    if not is_internet_connected():
        print(f"{str_prefix_err}You're not connected to the internet!")
        return 11 # Error code 11 = Try Again
    entries = []


    # ------------------------------------------------------------------------
    # TODO: The loop where you search all entries (may be Selenium).
    #       Fill into 'entries' variable. The goal is just to get the info into
    #       an array and process it all later since it'll be mixed in with
    #       Selenium code.
    # TODO: If this is a larger feed program, (1 web request/refresh per
    #       entry), remember to put in a check if it is in the file by UUID
    #       before going to that page. Something that can be generated/checked
    #       by just the table of contents/main list page of URLs.
    entries.append{
            'title': "", # Title of individual post
            'date': "", # Date of individual post
            'author': "", # Author of individual post. 'rss_author' if none
            'url': "", # URL of individual post
            'uuid': "", # UUID of individual post
            'description': "" # Description of individual post

            }
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # TODO: Process array of entries from gathered input (since at this point
    #       you grab everything without checking it exists first)
    #       Write entries -> FILTER CODE -> entries_filtered (same dict format)
    entries_filtered = []
    for entry in entries:
        # TODO: Replace entry['date'] with UTC format using datetime library
        # If it always comes in a predetermined format:
        #   entry['date'] = datetime.datetime.strptime(entry['date'], "%B %d, %Y /%H:%M%p")
        #   Below from https://docs.python.org/3/library/datetime.html
        #   %a: Weekday as locale’s abbreviated name. (Sun, Mon)
        #   %A: Weekday as locale’s full name. (Sunday, Monday)
        #   %d: Day of the month as a zero-padded decimal number. (30, 31)
        #   %b: Month as locale’s abbreviated name. (Jan, Feb)
        #   %B: Month as locale’s full name. (January, February)
        #   %m: Month as a zero-padded decimal number. (01, 02)
        #   %Y: Year with century as a decimal number. (2026)
        #   %H: Hour (24-hour clock) as a zero-padded decimal number. (00, 23)
        #   %I: Hour (12-hour clock) as a zero-padded decimal number. (01, 12)
        #   %p: Locale’s equivalent of either AM or PM. (AM, PM)
        #   %M: Minute as a zero-padded decimal number. (00, 59)
        #   %S: Second as a zero-padded decimal number. (00, 59)
        #   %Z: Time zone name (empty string if the object is naive). ([empty], UTC, GMT)
        # If there is no date, set to now.
        #   entry['date'] = format_datetime(datetime.datetime.now(datetime.timezone.utc), usegmt=True)

        bool_unique = True # TODO: replace 'unique' with the actual condition
        if bool_unique:
            entries_filtered.append(entry)

    # ------------------------------------------------------------------------

    # Write dict to JSON
    if bool_output_to_json:
        now = datetime.datetime.now().strftime("%Y %m %d %H%M%S")
        json_filename = f"{path}/{now} results.json"
        with open(json_filename, 'w') as fp:
            json.dump(book_sale_entries_dict, fp)
        if args.verbose:
            print(f"{str_prefix_info} Wrote to {json_filename}")

    # At this point, the JSON file is written. Now we can make the RSS feed
    to_rss.create_rss(rss_path, rss_title, rss_subtitle) # Create file if does not exist
    int_new_posts = 0
    for entry in entries_filtered:
        # Format the string of what will be the RSS description for better
        # reading in the Terminal
        _desc_tmp = entry['description']
        # _desc_tmp = erase_blank_lines(_desc_tmp)
        # _desc_tmp = _desc_tmp.replace("\n", ". ") # If needed
        # _desc_tmp = _desc_tmp.replace("", "")
        _desc_tmp = _desc_tmp.strip()
        entry['description'] = _desc_tmp
        # NOTE: variables with a single underscore as its first character are
        #   not copied over if this program is imported into something else.
        #   Ex. _array2 vs array2

        if not to_rss.check_post_exists(rss_path, entry['url'], entry['url']):
            # Duplicate post prevention. Only if matching URL and Description
            #   are already in the file. It's possible that this site reuses
            #   URLs, which is why I also want to check for matching
            #   descriptions. But the dates in the description would be
            #   different
            #   date_formatted = format_datetime(datetime.datetime.now(datetime.timezone.utc), usegmt=True)

            to_rss.add_to_rss(rss_path,
                              title=entry['title'],
                              author=entry['author'],
                              date=entry['date'],
                              url=entry['url'],
                              guid=entry['uuid'],
                              body=entry['description'])
            int_new_posts += 1
    if int_new_posts > 0:
        print("\t" + str(int_new_posts) + " new posts")
    return 0 # Completed successfully


if __name__ == "__main__":
    sys.exit(main())
    # Exit the program, returning the return code of main() - can be 1, 0, etc
