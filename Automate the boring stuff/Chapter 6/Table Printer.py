def printtable(table):
    colswidths = [0] * len(table)  # This variable will be used to store width of each column.
    # It stores a list containing the same number of 0 values as the number of inner lists in table data.
    # So if we have 3 inner lists it would be [0, 0, 0]

    # I am using max function with key=len on each list in the table to find the longest string
    # --> it's length be the length of the column
    for x in range(len(table)):  # Loop through the number of lists we have.
        colswidths[x] = len(max(table[x], key=len))
        # So let's say i = 0
        # This will grab the 1st list in the table and look at the length of each object in that list.
        # (That's what the key = len bit does - tells the max function to look at each item in the list)

    # Looping through the table to print columns
    for c in range(len(table[0])):  # This will just loop through the number of VALUES in the 1st list.
        # It will give us the number of COLUMNS we need.
        for r in range(len(table)):  # This will go through the number of lists that are stored.
            # This will give us the number of ROWS
            print(table[r][c].rjust(colswidths[r], " "), end=" ")
            # By swapping the indexes over we work DOWN the array, not across.
            # Each entry is right justified and has a number of spaces added to it's left to pad it out.
            # The number of spaces added is equal to the colsWidths entry that matches the longest item in that list.
            # The END parameter tells print NOT to print a new line but to print a space after.
            # So that's how we get the items listed one after another.
        print("")


tabledata = [["apples", "oranges", "bananas"],
             ["1", "2", "3"],
             ["Dog", "Cat", "Bat"]]

printtable(tabledata)
