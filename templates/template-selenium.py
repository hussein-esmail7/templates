'''
[FILENAME]
[AUTHOR]
Created: [DATE]
Updated: [DATE]
Description: [DESCRIPTION]
'''

# This part is used for https://github.com/hussein-esmail7/template-maker
# templateDescription: Python Selenium Web Scraper

import os
import sys # To exit the program
from selenium import webdriver
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select  # Used to select from drop down menus
from selenium.webdriver.chrome.service import Service # Used to set Chrome location
from selenium.webdriver.chrome.options import Options # Used to add aditional settings (ex. run in background)
from selenium.webdriver.common.by import By # Used to determine type to search for (normally By.XPATH)
# from selenium.webdriver.common.keys import Keys  # Used for pressing special keys, like 'enter'

# ========= VARIABLES ===========
bool_run_in_background  = True
target_site             = "https://google.com"

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

def main():
    options = Options()
    if bool_run_in_background:
        options.add_argument("--headless")  # Adds the argument that hides the window
    service = Service(ChromeDriverManager(log_level=0).install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(200, 1000) # Window size
    driver.get(target_site)

    # ADDITIONAL CODE HERE
    # Example of getting elements by XPATH -----------------------------------
    # ITEM = driver.find_element(By.XPATH, '//time/span[1]')        # singular
    # ITEM = driver.find_elements(By.XPATH, '//time/span[1]')        # n items
    # Example of getting elements by CLASS_NAME ------------------------------
    # ITEM = driver.find_element(By.CLASS_NAME, 'schedule')         # singular
    # ITEM = driver.find_elements(By.CLASS_NAME, 'schedule')         # n items
    # Example of getting elements by ID --------------------------------------
    # ITEM = driver.find_element(By.ID, 'schedule')                 # singular
    # ITEM = driver.find_elements(By.ID, 'schedule')                 # n items
    # Example of getting elements by TAG_NAME --------------------------------
    # ITEM = driver.find_element(By.TAG_NAME, 'div')                # singular
    # ITEM = driver.find_elements(By.TAG_NAME, 'div')                # n items
    # Example of getting text from an element --------------------------------
    # ITEM = driver.find_element(By.CLASS_NAME, 'schedule').text
    # NOTE: If .text is run on a list, it may give an error or parse the entire
    #   thing by itself. Best to run this in a loop if doing it for every
    #   element.

    dummy = input("Program is up to date. Press enter to quit > ")
    # Put this line where you need to have time to inspect the site
    # If printing information to process, print it before this 'dummy' line.
    # The final finished program should not have this line by the time you're
    # dont writing it, only for purposes while writing the program

    # Cleanup
    driver.close()  # Close the browser
    options.extensions.clear() # Clear the options that were set
    sys.exit() # Exit the program

if __name__ == "__main__":
    main()
