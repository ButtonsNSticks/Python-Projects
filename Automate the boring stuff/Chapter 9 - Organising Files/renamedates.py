#! python3
#  renamedates.py - Renames file names with american MM-DD-YYYY date format to European date format DD-MM-YYYY

# Import modules
import os  # Needed to interact with PC file system.
import re
import shutil  # Needed to make copies of files etc.

# Define regular expression (RegEx) that matches files with the American date format.

datepattern = re.compile(r'''
    ^(.*?) 
    # The .* says "find all text" but the ? forces Python to do a "non greedy search"
    # Returning the shortest possible string
    (\d{1,2})- # Match 1 or two didgets for the MONTH followed by a -
    (\d{1,2})- # Match 1 or 2 didgets for the DAY followed by a -
    (\d{1,4})  # Match 4 didgets for the year
    (.*?)$     # Grab any text at the end after the YEAR
    ''', re.VERBOSE)  # The Re.Verbose is needed to tell python to ignore the comments above!

#  Todo: Loop over the files in the working directory.
for americanfilename in os.listdir("."):
    #  Gets all the files in the current working directory, puts them in a list & loops though them...
    mo = datepattern.search(americanfilename)
    # Searches the current file name to see if it matches the regex defined in "datepattern".
    # If it does it will return the result to the variable mo (Match Object)

    if mo is None:
        # If the current file doesnt match the reg ex then the mo variable will be empty so we can ignore it
        continue

    # Otherwise we DO have a match - so lets grab the different bits of the file name (DD, MM, YYYY etc).
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(3)
    yearpart = mo.group(4)
    afterpart = mo.group(5)

    # Form the EU style filename
    eurofilename = beforepart + daypart + "-" + monthpart + "-" + yearpart + "-" + afterpart
    # Join all of the different bits up to make the new EU file name.

    # Get the full absolute file path
    absworkingdir = os.path.abspath(".")  # Get the absolute path of the current working directory.
    americanfilename = os.path.join(absworkingdir, americanfilename)
    # Get the absolute path of the current USA file being worked on eg: C:\some directory\usa-MM-DD-YYYY
    eurofilename = os.path.join(absworkingdir, eurofilename)
    # Get the absolute path of the new EU formatted file to be made eg: C:\some directory\eu-DD-MM-YYYY

    # Rename the files
    print("Renaming '%s' to '%s'..." % (americanfilename, eurofilename))
    shutil.move(americanfilename, eurofilename) # Uncomment AFTER testing!
