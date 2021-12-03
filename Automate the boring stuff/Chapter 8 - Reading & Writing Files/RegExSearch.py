#! python3
#  This script will search all .txt files in a given directory for text which matches a regular expression.
#  The regular expression is defined via user input.
#  It then prints out what it finds in the runtime window.

# Import Modules
import os
import re

folder_name = "textfiles"  # The name of the folder with the text files in.

path_to_files = os.path.join(os.getcwd(), folder_name)  # Makes the full path to the files

# Ask the user to enter a regular expression & turn it into a string.
userregex = str(input("Please enter a regular expression:\n"))

# Turn the users input INTO a regular expression
userregex = r"%s" % userregex  # Adds the r" and swaps out %s for the regular expression the user typed.

userregex = re.compile(userregex, re.IGNORECASE)  # The re.IGNORECASE is there to provide matches to all CaPs.

for filename in os.listdir(path_to_files):  # Work through each file in the folder

    path_to_filename = os.path.join(path_to_files, filename)  # Build the full path of the file being looked at.

    with open(path_to_filename, 'r') as file:  # Opens the file being looked at as READ only.
        file_content = file.read()  # Get the content of the file.
        matched_text = userregex.findall(file_content)  # Find all match in the text file.

        if matched_text is not None:
            print("\nMatches found in " + filename + ":")
            for match in matched_text:
                print(match)
