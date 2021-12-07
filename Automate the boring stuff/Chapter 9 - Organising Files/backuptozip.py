#! python3
# backuptozip.py - Copies an entire folder and its contents into a zip file whose filename increments.

# Import modules
import os  # Allows us to work with the PC's operating system
import zipfile  # Allows us to ZIP files up


def backuptozip(folder):  # Defines a function which takes in a STRING value "folder"
    folder = os.path.abspath(folder)  # Gets the absolute path of the folder

    number = 1
    while True:  # This will run forever until we break out of it.
        zipfilename = os.path.basename(folder) + "-" + str(number) + ".zip"
        # The os.path.basename(folder) will return just the name of the folder from the absolute path.
        # The str(number) converts the number into a string value
        # So here we set the zip file name to be the folder name plus a number e.g "Folder name - 1.zip"

        if not os.path.exists(zipfilename):  # If the zipfile does NOT exist then...
            break  # Exit the loop
        number += 1
        # If the path DOES already exist (e.g "Folder name - 1.zip)
        # Then we need to add 1 to the variable number and then repeat the while loop to change the zipfile
        # name to "Foldername - 2.zip" and try again. If THIS exists then try "Foldername - 3" and so on.

    # Make the zip file
    print("Creating %s" % zipfilename)
    backupzip = zipfile.ZipFile(zipfilename, "w")
    # Makes the zipfile & opens it in WRITE mode so we can add things to it.
    # Assigns it to a variable "backupzip" so we can reference and work with in via code.

    # Walk the entire folder tree and compress everything
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % foldername)
        # Add the current folder to the ZIP file
        backupzip.write(foldername)

        # Add all the files in the folder to the ZIP file
        for filename in filenames:  # This will loop through all of the files in the current folder
            newbase = os.path.basename(folder) + "_"  # Grabs the filename & adds a "-" to the end.
            if filename.startswith(newbase) and filename.endswith(".zip"):
                # We don't want to add previously made backups to the new one
                # So here we look to see if the file name is a zip file and if so, skip it.
                continue  # Ends this loop and starts over
            backupzip.write(os.path.join(foldername, filename))  # Add the file to the zip
    backupzip.close()  # Close the zip file.

    print("Done")


backuptozip("D:\\delicious")  # Call the function

