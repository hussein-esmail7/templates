"""
Voice Program
Hussein Esmail
Created: 2018 04 23
Updated: 2020 12 27
Description: This program says whatever is inputed in its arguments via the terminal 'say' command.
"""

import os
import sys

os.system('say ' + " ".join(sys.argv[1:]))

