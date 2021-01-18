#!usr/local/bin/python3
"""
Base 64 Converter
Hussein Esmail
Created: February 8, 2020
Updated: June 23, 2020
Description: This program inputs a base64 string and returns it's decrypted form.
"""

import base64                   # To convert the base64s
import sys                      # To exit the program
from termcolor import colored   # For colored output
import requests                 # To check if string is a url
import webbrowser               # Opens url if it is a url

first_run = True
encoding = "utf-8"
color_output = "cyan"
color_title = "red"
title = "Base64 Converter"

intro = """To convert multiple encodes in one line, follow this format:
    <base64 1> + <base64 2> + ...
Type 'exit' or 'exit()' to exit this program"""

print(colored(title, color_title))
print(intro)
while True:
    base64s_to_convert = [] # Unconverted base64s will be stored here
    converted = "" # Appends to this string, so it must be empty at the start of every loop run
    bool_is_correct_format = True # Used if there are multiple entries. It's correct until it's not
    if first_run:
        first_run = False
        if len(sys.argv) > 1:
            input_str = " ".join(sys.argv[1:])
            print("> " + input_str)
        else:
            input_str = input("> ")
    else:
        input_str = input("> ")
    if input_str == "exit" or input_str == "exit()": # If the user typed the exit command
        sys.exit()
    input_array = input_str.split(" ")
    if len(input_array) > 1:
        for i in range(1, len(input_array), 2): # check every other entry is "+"
            if input_array[i] != "+":
                bool_is_correct_format = False
        if bool_is_correct_format:
            for i in range(0, len(input_array), 2): # for all the base64s
                base64s_to_convert.append(input_array[i])
        else: # If the format was not correct
            print("ERROR: Input not formatted properly")
    else: # If only one base64 was entered
        base64s_to_convert.append(input_str)
    
    for i in base64s_to_convert:
        try:
            converted += base64.b64decode(i).decode(encoding)
        except Exception as e:
            print(e)
            print("ERROR: " + i + " is not a base64")
    if len(converted) != 0:
        print(colored("> ", color_output) + converted)
        
    bool_continue = True
    converted2 = converted
    while bool_continue: # In case it is x2 or x3 or ...
        try:
            converted2 = base64.b64decode(converted2).decode(encoding)
            print(converted2)
        except:
            bool_continue = False
    try: # Check if it is a link. If it is, open it
        check_str_for_url = requests.get(converted2)
        print(colored("> ", color_output) + "Base64 is a URL. Opening...")
        # Opens in a browser that is already open (doesn't have ot be default). If none is open, it will use default
        webbrowser.open_new_tab(converted2)
    except:
        pass
