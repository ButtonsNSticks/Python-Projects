#! python3
# remove_CSV_header.py - Removes the header from all CSV files the in current working directory

import csv
import os

""" Makes the header_removed directory, 
the exist_ok=True bit says "its ok if it already exists! """

os.makedirs("header_removed", exist_ok=True)

# Loop through every file in the current working directory.

for csv_file in os.listdir("."):
    if not csv_file.endswith(".csv"):
        continue  # Skip over the non csv files - start the FOR loop again.

    print("Removing header from {}...".format(csv_file))

    # Read the CSV file in, skip the 1st row.
    csvRows = []  # Set up empty list.

    with open(csv_file) as csv_file_object:
        reader_object = csv.reader(csv_file_object)  # Pass the CSV file into the CSV reader.

        for row in reader_object:  # Look at each row.
            if reader_object.line_num == 1:  # If it's the 1st row then...
                continue  # Skip the 1st row.
            csvRows.append(row)  # Otherwise, add the row into the csvRows list.

        # Write out the CSV file.

        full_path = os.path.join("header_removed", csv_file)  # Define the full path.

        with open(full_path, "w", newline="") as file:  # Open up the new file in WRITE mode.
            csv_writer = csv.writer(file)  # Set up the CSV writer to write to the file.
            for row in csvRows:  # Loop through each of the rows stored in csvRows
                csv_writer.writerow(row)  # Write them to the file.
