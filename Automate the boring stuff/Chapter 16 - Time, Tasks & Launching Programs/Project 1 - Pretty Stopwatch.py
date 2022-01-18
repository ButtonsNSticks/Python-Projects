#! python3
# stopwatch.py - A simple stopwatch program

"""Challenge: 1) Expand the stopwatch project so that it uses the rjust() and ljust() string methods
to make the output look nicer.
2) Use the pyperclip module to copy the text output to the clipboard."""

# Import modules

import pyperclip
import time

# Step up Global Variables

start_time = time.time()  # Get the start time
last_time = start_time
lap_no = 1
text_to_paste = ""  # This is where we will store the entire string to paste into pyperclip

# Display the instructions

print("Press ENTER to begin. Afterwards, press ender to 'click' the stopwatch\nPress CTRL+C to quit")

input()  # Press Enter to begin

print("Started")

# Start tracking the lap-times
try:

    while True:  # Sets a loop that goes on forever...
        input()  # Waits for the user to hit enter again.
        lap_time = round(time.time() - last_time, 2)
        # When they do, calculate how many seconds have passed for THIS lap - round to 2dp.

        total_time = round(time.time() - start_time, 2)

        # This works out how many seconds have passed IN TOTAL from the start until now.

        """ This is the extra code added to complete the challenge.
        1st we output the results as formatted strings"""

        # Get string versions of the times
        str_lap_no = "Lap # {}:".format(str(f"{lap_no:02d}"))  # This adds a leading 0 to numbers less than 10.
        str_total_time = str(total_time).rjust(6, " ")
        str_lap_time = "(" + str(lap_time).rjust(6, " ") + ")"

        # Todo: Make the text to paste into a string
        output_string = str_lap_no + str_total_time + " " + str_lap_time

        print(output_string, end="")

        # todo: Add the string to the total text to paste & pass to Pyperclip

        text_to_paste += output_string + "\n"

        """End of extra code to format the strings"""

        # print("Lap{}: {} ({})".format(lap_no, total_time, lap_time), end="")

        lap_no += 1  # Increase the lap number by 1.
        last_time = time.time()  # Reset the last lap time.

except KeyboardInterrupt:  # If a Keyboard Interrupt error occurs (use hits CTRL & C) then...
    print("\nDone.")
    pyperclip.copy(text_to_paste)
