from selenium import webdriver
from selenium.common.exceptions import *
# from selenium.webdriver.support.ui import Select  # Used to select from drop down menus
from selenium.webdriver.chrome.options import Options  # Used to add aditional settings (ex. run in background)
# from selenium.webdriver.common.keys import Keys  # Used for pressing special keys, like 'enter'
import sys # To exit the program

bool_use_Brave = True
bool_run_in_background = True
chromedriver_path = "/Users/hussein/Downloads/chromedriver"
target_site = "https://google.com"

options = Options()  
if bool_run_in_background:
    options.add_argument("--headless")  # Adds the argument that hides the window
if bool_use_Brave:
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    driver = webdriver.Chrome(options=options)
else:
    driver = webdriver.Chrome(chromedriver_path, options=options)
driver.get(target_site)

# ADDITIONAL CODE HERE

# Cleanup
driver.close()  # Close the browser
options.extensions.clear() # Clear the options that were set
sys.exit() # Exit the program
