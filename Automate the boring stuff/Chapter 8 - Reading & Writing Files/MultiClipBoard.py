#! python3
# mcb.pyw - Save and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves the clipboard to the keyword.
# Usage: py.exe mcb.pyw <keyword> - Loads the keyword to the clipboard
# Usage: py.exe mcb.pyw list - Loads all keywords to clipboard.

# Import the modules

import pyperclip  # Needed as we will be copying and pasting to and from the clipboard.
import shelve  # Needed to save the data that's copied
import sys  # Needed to read command line arguments passed to the script.

mcbshelf = shelve.open('mcb')  # Makes a shelve file called mcb for this program.

# Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower == "save":
    # sys.argv is a list of strings.
    # Each item in the list is one of the arguments that was passed on the command line.
    # sys.arg[0] is the name of the script ie mcb.pyw
    # sys.arg[1] is the 1st argument that's passed, so it could be "save" or "list" or the keywords.
    # So here we check to see if the sys.arg[1] is save and also that there are 3 things:
    # 0 = the script name 1 = save 2 = keyword
    # If the user has opted to save then sys.argv[2] will be the keyword they want to use, so then we do...

    mcbshelf[sys.argv[2]] = pyperclip.paste()

    # Copy what is in the clipboard into the shelf file with the "Key" being the keyword that was given
    # By the user which is saved in sys.argv[2]

elif len(sys.argv) == 2:
    # If the number of arguments stored in sys.argv list is 2
    # Then the user has (probably) typed "mcb.pyw list" OR "mcb.pyw <keyword>"
    # sys.argv[0] is the script name "mcb.pyw"
    # sys.argv[1] is (hopefully) the word "list" or a keyword to retrieve previously saved stuff.

    # Check if the user typed LIST
    if sys.argv[1].lower() == "list":  # Checks to see if the lowercase version of the argument is "lower"
        pyperclip.copy(str(list(mcbshelf.keys())))
        #  This grabs all of the keys stored in the shelf file and turns them into a list.
        # It then turns the list into a string
        # Finally it copies the string into the clipboard of the computer.

    # If they didn't type SAVE or LIST then they want to save the text using the keyword they used instead.

    elif sys.arg[1] in mcbshelf:
        # This checks to see if the argument passed is already a key in the mcbshelf file.
        # If it is then this means the user has previously saved some text under this keyword.
        # So now we will get it back
        pyperclip.copy(str(list(mcbshelf[sys.arg[1]])))

mcbshelf.close()  # Closes the shelve file
