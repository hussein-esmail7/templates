# QR Code Generator in Python

"""
QR Code Generator
Hussein Esmail
Created: 2020 12 11
Updated: 2020 12 23
Description: This program converts given text or clipboard to a QR code then 
    opens the image in the default image viewer
"""

import pyqrcode         # Used to generate QR Code
import pyperclip        # Used to get clipboard if user wants to convert the clipboard
import sys              # Used to exit the program and get the playform type
import subprocess       # Used to run terminal commands to open the generated image

def main():
    # os.chdir("~/Downloads")
    image_name = "qr.png"
    if len(sys.argv) < 2:
        print("Please input a string to convert to QR!\nType 'clipboard' to copy from clipboard")
    else:
        if (sys.argv[-1] == "clipboard"):
            convert = pyperclip.paste()
        else:
            convert = " ".join(sys.argv[1:])
        url = pyqrcode.create(convert)
        url.png(image_name, scale = 8)
        subprocess.run([{   'linux':    'xdg-open',
                            'win32':    'explorer',
                            'darwin':   'open'}     [sys.platform], image_name])
    sys.exit()

if __name__ == "__main__":
    main()