#!/bin/bash

# === PROGRAM DESCRIPTION ===
# This program generates a template 
# file for the chosen file type

# Make sure the bash version is compatible with this program
case $BASH_VERSION in 
    ''|[0-3].*) echo "ERROR: Bash 4.0+ required" >&2; exit 1;; 
    esac

# Prompt text. The variable must be named 'PS3' for it to work.
# Make sure there is a trailing space at the end or it will look weird
PS3='Please enter your file type choice: '
# For those interested:
#   PS1 is the line in terminal that asks for your commands normally. Usually it's "username: current_directory"
#   PS2 is the line that asks you to keep typing if you type a command with open quotes or something like that

# Today's date, used for file creation date section. You can also change 
# the date format by reading the manual page at 'man date'
date=$(date '+%Y %m %d')   

# Full name of the user, used in AUTHOR sections of the file that is going to be created.
username=$(id -F)
# TODO: If this cannot be run, run $(whoami) instead

# Varialbe for the file name will be stored here
file_name=""

# List of file types to ask
# The StackExchance answer I found this from also 
# included a 'Quit' option but the user can just press ^C || ^D
options=(".c (C)"
        ".cpp (C++)"
        ".css (CSS)"
        ".html (HTML)"
        ".java (Java)"
        ".ms (Groff)"
        ".py (Python)"
        ".sh (Shell Script)")

# This section of code is so that you don't need to retype all the entries in the 
# case statement, instead use indexes
declare -A options_reverse=()       # Create an associative array
for idx in "${!options[@]}"; do     # For each item in the options array
  val=${options[$idx]}              
  options_reverse[$val]=$idx        # entry of $options is = index, number = the value
done

# This function finds a filename that does not exist already so it doesn't override any existing files
function name_that_file() { 
    # ${1} = file name without extension
    # ${2} = file extension without the ".". (Ex: a Python file will be "py", not ".py")
    template_name="${1}.${2}"
    counter=0
    if [ -f "$template_name" ] ; then               # If the file already exists in the directory
        while [ -f "$template_name" ] ; do          # While the next file exists, find another name  
            ((counter=counter+1))                   # Add 1 to the name counter
            template_name="${1} ($counter).${2}"    # Make a new name (wikk check on next loop)
        done                                        # Exits loop when it found an unused name
        file_name="$template_name"                  
    else                                            # If the original file name is available
        file_name="${1}.${2}"
    fi
}

select option in "${options[@]}" # Asks for the option choice
do
    # case $option in 
    case "${options_reverse[$option]}" in
        0) # C programming file
            name_that_file "template" "c"
            printf "#include <stdio.h>\n#include <string.h> // Used for strings, checking equalness, copying strings, etc.\n\n/*\n%s\n%s\nCreated: %s\nUpdated: %s\nTerminal command to compile file to an executable:\n    gcc -o name filename.c\n    ./name\nTerminal command to compile multiple files into one executable:\n    gcc -Wall name filename.c\n    ./name\nDescription: [DESCRIPTION]\n*/\n\nint main(void) {\n   // CODE HERE\n   \n   return 0;\n}\n" "$file_name" "$username" "$date" "$date" > "$file_name"
            exit 0
            ;;
        1) # C++ programming file
            file_name=name_that_file "template" "cpp"
            printf "#include <cstdio>\n#include <cstdlib>\n#include <iostream>\nusing namespace std;\n\n/*\n%s\n%s\nCreated: %s\nUpdated: %s\nTerminal command to run file:\n    g++ -o name filename.cpp && ./name\nDescription: [DESCRIPTION]\n*/\n\nint main(int nNumberOfArgs, char* pszArgs[]) {\n    // CODE HERE\n    return 0;\n}" "$file_name" "$username" "$date" "$date" > "$file_name"
            exit 0
            ;;
        2) # CSS programming file
            file_name=name_that_file "style" "css"
            printf "/*\n%s\nWritten by %s\nCreated: %s\nUpdated: %s\n*/\n\n.body {\n}\n" "$file_name" "$username" "$date" "$date"> "$file_name"
            exit 0
            ;;
        3) # HTML File
            file_name=name_that_file "index" "html"
            printf "<!DOCTYPE html>\n<html lang=\"en\">\n\n<head> <!-- HEADER -->\n    <title>TITLE OF PAGE</title> <!--TODO: Title of page-->\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" media=\"screen\"/>\n    <meta charset='utf-8'>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n</head> <!-- HEADER (end) -->\n<body class=\"background\">  <!-- BODY -->\n	<div class=\"topnav\">\n        <!-- TODO: Navigation bar\n		<a class=\"active\" href=\"#\">THIS PAGE NAME ON MENU BAR</a>\n		<a href=\"URL.html\">OTHER PAGES IN NAVE BAR</a>\n        -->\n	</div>\n    <!-- TODO: CODE HERE (rest of content) -->\n    \n</body> <!-- BODY (end) -->\n<footer style=\"font-size: small;\">  <!-- FOOTER -->\n    <p>\n        <!--TODO: Email here-->\n        Send me an <a href=\"mailto:EMAIL\" class=\"url\">email</a>!\n    </p>\n</footer> <!-- FOOTER (end) -->\n</html>" > "$file_name"
            exit 0
            ;;
        4) # Java programming file
            file_name=name_that_file "template" "java"
            printf "package %s;\n\n/*\nProgram Name: %s\nCreated by: %s\nCreated: %s\nUpdated: %s\nDescription: [DESCROPTION]\n */\n\npublic class %s { \n	\n	/**\n	 * @author %s\n	 * @param args\n	 */\n	public static void main(String[] args) {\n		// Code here\n		\n		\n	}\n	\n}\n" "${file_name%.*}" "$file_name" "$username" "$date" "$date" "${file_name%.*}" "$username" > "$file_name"
            exit 0
            ;;
        5) # Groff markup file
            file_name=name_that_file "template" "ms"
            printf ".TL\n%s\n.AU\n%s\n.PP\nThis is a generic paragraph" "$file_name" "$username" > "$file_name"
            exit 0
            ;;
        6) # Python programming file
            file_name=name_that_file "template" "py"
            "import os, sys\n\n'''\n%s\n%s\nCreated: %s\nUpdated: %s\nDescription: [DESCRIPTION]\n'''\n\ndef main():\n    # CODE HERE\n    sys.exit()\n\n\nif __name__ == \"__main__\":\n    main()\n" "$file_name" "$username" "$date" "$date" > "$file_name"
            exit 0
            ;;
        7) # Bash shell script
            file_name=name_that_file "template" "sh"
            printf "#!/bin/bash\n\n: ' %s\n%s\nCreated: %s\nUpdated: %s\nDescription: [DESCRIPTION]\n'\n\n# CODE HERE\n\nexit 0\n" "$file_name" "$username" "$date" "$date" > "$file_name"
            exit 0
            ;;
        *) echo "Invalid option: '$REPLY'";;
    esac
done

exit 0

