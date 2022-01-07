""" Write a program to read in the contents of several files and insert the contents into a spreadsheet.
One line of text per row.
Lines of text file 1 will be in Col A
Lines of text file 2 in Col B and so on"""

from openpyxl import Workbook

# Define the text files

file1 = "Text1.txt"
file2 = "Text2.txt"
file3 = "Text3.txt"

filelist = [file1, file2, file3]

wb = Workbook()  # Make a new workbook.
ws = wb.active  # Go to the 1st sheet

# Read in the text line by line

for i in range(len(filelist)):
    with open(filelist[i]) as f:
        for count, line in enumerate(f):
            #print(count, line)

            ws.cell(row=(count+1), column=i+1).value = line

"""Save the file"""

wb.save("TextFile.xlsx")
