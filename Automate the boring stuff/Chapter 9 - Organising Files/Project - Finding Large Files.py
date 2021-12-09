#! python3
# Write a program that walks through a folder tree and searches for exceptionally large files
# or folders — say, ones that have a file size of more than 100MB.

# Import modules
import os
import shutil

# Define the minimum size of file that you want to look for in mb
min_size_mb = 100
min_size_bytes = min_size_mb * 1000000

#  Define the path to use - it will be the same directory the pyton file is in.

script_path = os.path.dirname(__file__)  # This is the ABSOLUTE path

# Walk through the folder tree

for path, sub_folders, files in os.walk(script_path):

    folder_size=0 # Sets the size counter to 0 for the current folder we are looking at.

    # Deal with large files 1st

    for file in files:

        file_path = os.path.join(path, file)  # Get the absolute path to current file
        file_size = os.path.getsize(file_path)  # Get the size of the current file
        sub_dir = os.path.basename(path)  # Get the name of the directory the current file is in

        if file_size >= min_size_bytes:  # If the current file size is greater than or equal to our min_file_size

            file_size_mb = file_size / 1000000  # Work out file size in Mb

            folder_size += file_size  # Add the size of the file to the counter.

            print("LARGE FILE FOUND -> Path: " + path + " File: " + file + " | Size: " + str(file_size_mb) + " Mb")
            # Print out the file name and size.

    if folder_size >= min_size_bytes: # If the folder counter is equal to or > than the minimum size we set...

        print("LARGE FOLDER FOUND -> Folder: " + path + " | Size: " + str(folder_size) + " Mb")
