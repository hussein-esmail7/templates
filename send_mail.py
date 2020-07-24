
"""
Email sender template
Created by Hussein Esmail
Description: This program is a template if someone wants to send an email 
    through a program. You would hust have to replace the input variables.
    Feel free to provide anything that can help this program!

"""

import smtplib
import ssl
import getpass
import sys

try:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = input(f"Your email: ")
    password = getpass.getpass(f"Password for {sender_email}: ")
    receiver_email = input("Recipient email: ")
    message = input("Message:\n")
    send_ask = input("Send? [y/n]: ")
    if send_ask.lower() != "n":
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password) # Login to email
            server.sendmail(sender_email, receiver_email, message) # Send the email
        print("Email sent") # Notify the user
except smtplib.SMTPAuthenticationError: # Password was wrong
    print("Incorrect username or password.")
    
