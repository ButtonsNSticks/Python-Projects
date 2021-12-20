#! python3
# mapit.py - Launches a map in the browser using and address from the clipboard or command line

import pyperclip # Needed for copying and pasting
import sys  # Needed to handle command line arguments
import webbrowser  # Needed to launch the web browser

"""The command line arguments will be stored in the variable sys.argv.
The 1st item in the sys.argv list should always be a string containing the program’s filename
('mapit.py'), and the 2nd item should be the first command line argument, the third item is the 2nd argument
and so on.

Command ine arguments are separated by spaces - but here we need ALL of them in ONE string to pass to
Google Maps. As sys.argv is a list of strings, we can join them together using the .join method.
As sys.argv[0] is the name of the script, we don't want that but we do want all of the other items in the list
so we need to use sys.argv[1:] as this will give us the 2nd item in the list and all others which follow."""

if len(sys.argv) > 1:  # Check to see if an argument has been passed
    # Get address from the command line
    address = " ".join(sys.argv[1:])
    # The " " is the delimiter which will be used in between each string that's joined.

else:
    # Get address from clipboard
    address = pyperclip.paste()

# Open Google Maps

webbrowser.open("https://www.google.com/maps/place/" + address)

