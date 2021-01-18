# Templates

Hello! This repository is mainly for myself for files I might need time and time again. Though it is fine for you to use. If you have anything you think you can contribute, please help my code be better!

## requirements.txt
This file is all the requirements for all of the python files here. To use this file, download it and run 'pip3 install requirements.txt' in the same directory as the file, and you should have no ModuleNotFoundError issues.

## base64convert.py
This file converts a base64 text to a text readable by the user (either by typing it in the arguments of the file or in its input field). If it is a URL, it will open it in the default browser.

## cli.py, cli.java
These files asks for input infinite amount of times until the user types one of the exit commands ("exit", "q", "quit", etc.) (the .java file currently only supports "exit"). This is mainly used for interface programs, that would take many commands within the program. 

## password_generator.py
This program generates a random password that can be used when creating internet accounts. If a number is typed along with the 'python3 password_generator.py', it will make a password of that length. For example: 'python3 password_generator.py 10'.

## template.cpp, template.tex
These files are basic boilerplate files for C++ and LaTeX (a typesetting system) so you can get working on the important stuff faster.

## QR.py
This program converts given text or clipboard to a QR code then opens the image in the default image viewer regardless of your operating system.
    
## selenium_template.py
This program is a template for interacting with websites using selenium. This also has the capability of running the programs in the background so you don't have to see the webpages as it runs.

## send_mail.py
This program is a template if someone wants to send an email through a program. You would just have to replace the input variables.

## voice.py
This program says whatever is inputed in its arguments via the terminal 'say' command.

## vtt.py
This program inputs a .vtt subtitle file, and asks for a time delay: HH:MM:SS:MS and outputs a new .vtt file with the time delay factored into every line.
