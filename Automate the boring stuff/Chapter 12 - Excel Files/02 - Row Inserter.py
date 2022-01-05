""" Challenge: Takes 2 integers N & M and the name of an existing Excel file.
It then inserts M blank rows at row N"""

# ! python3

# Import Modules
from openpyxl import load_workbook
import os  # Needed to check if a file exists
import sys  # Needed to take in command line arguments

# Global Variables
script_path = os.path.dirname(__file__)  # This is the ABSOLUTE path

"""Check that user has entered two integers N & M from the command line, quit if not."""

if len(sys.argv) < 4:
    print("Usage: BlackRowInserter.py N M Filename.XLSX  -  Where N and M are a whole numbers")
    sys.exit()
else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    sheet = str(sys.argv[3])

""" Check the file exists"""

if os.path.isfile(sheet):
    wb = load_workbook(filename=sheet)
else:
    print("File {} not found".format(sheet))
    sys.exit()

"""Get Active WorkSheet"""

ws = wb.active
ws.insert_rows(n, m)

"""Save the file"""

wb.save("Updated.xlsx")
