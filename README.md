# Templates
Hello! This repository is mainly for myself for files I might need time and
time again. Though it is fine for you to use. If you have anything you think
you can contribute, please help my code be better!

# Table of contents
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Using These Files](#using-these-files)
- [File Descriptions](#File-Descriptions)
    - [[LaTeX] Captions Template](##captions-template.tex)
    - [[LaTeX] General Template](##template.tex)
    - [[LaTeX] Lecture Notes Template](##lecture-template.tex)
    - [[LaTeX] Script Template](##script-template.tex)
    - [[py, java] CLI Templates](##cli.py,-cli.java)
    - [[py] .vtt Subtitle Time Editor](##vtt.py)
    - [[py] Automated Email](##send-mail.py)
    - [[py] Base64 Converter](##base64convert.py)
    - [[py] Password Generator](##password-generator.py)
    - [[py] QR Code Generator](##QR.py)
    - [[py] Say Text Aloud](##voice.py)
    - [[py] Selenium Template](##selenium-template.py)
    - [[sh] Template Generator Program](##template.sh)
    - [[txt] Requirements](##requirements.txt)
- [Donate](#donate)

# Installation
Copy and paste this command to download this repository after you've changed
directories to the folder you want.

```
git clone https://github.com/hussein-esmail7/templates
cd templates/
pip install requirements.txt
```

If you want to run one of the python files and have python3 installed, you can
install the required libraries via pip using the last line.

# Using These Files
I use this repository via the
[template-maker](https://github.com/hussein-esmail7/template-maker) program
which has a Terminal user interface and gets the chosen file type from this
repository. I recommend you check it out. You can also configure that program
to use your own template files as well.

# File Descriptions
## captions-template.tex
Template document for Theatre Accessibility Performance Captions because typing
the script in LaTeX is faster than centering text in PowerPoint in each slide.
[A PDF example can be found
here](https://github.com/hussein-esmail7/templates/blob/master/LaTeX%20PDF%20Examples/captions-template.pdf).

## template.tex
This file is a basic boilerplate file LaTeX (a typesetting system) so you can
get working on the important stuff faster.

## lecture-template.tex
This file is written in LaTeX, and is meant to have all the lecture notes for a
specific class during my time at university.

## script-template.tex
Template document for a theatre performance script. [A PDF example can be found
here](https://github.com/hussein-esmail7/templates/blob/master/LaTeX%20PDF%20Examples/script-template.pdf).

## cli.py, cli.java
These files asks for input infinite amount of times until the user types one of
the exit commands ("exit", "q", "quit", etc.) (the .java file currently only
supports "exit"). This is mainly used for interface programs, that would take
many commands within the program. 

## vtt.py
This program inputs a .vtt subtitle file, and asks for a time delay:
HH:MM:SS:MS and outputs a new .vtt file with the time delay factored into every
line.

## send-mail.py
This program is a template if someone wants to send an email through a program.
You would just have to replace the input variables.

## base64convert.py
This file converts a base64 text to a text readable by the user (either by
typing it in the arguments of the file or in its input field). If it is a URL,
it will open it in the default browser.

## password-generator.py
This program generates a random password that can be used when creating
internet accounts. If a number is typed along with the 'python3
password-generator.py', it will make a password of that length. For example:
'python3 password-generator.py 10'.

## QR.py
This program converts given text or clipboard to a QR code then opens the image
in the default image viewer regardless of your operating system.

## voice.py
This program says whatever is inputted in its arguments via the terminal 'say'
command.

## selenium-template.py
This program is a template for interacting with websites using selenium. This
also has the capability of running the programs in the background so you don't
have to see the webpages as it runs.

## template.sh
This program is not just a simple template shell script. This program lets you
choose what file type you want generated and makes that template file. The
current options are .c (C), .cpp (C++), .css (CSS), .html (HTML), .java (Java),
.ms (Groff), .py (Python), .sh (Bash)

## requirements.txt
This file is all the requirements for all of the python files here. To use this
file, download it and run 'pip3 install requirements.txt' in the same directory
as the file, and you should have no ModuleNotFoundError issues.

# Donate
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/husseinesmail)
