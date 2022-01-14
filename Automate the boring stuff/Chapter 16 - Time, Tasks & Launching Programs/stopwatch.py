#! python3
# stopwatch.py - A simple stopwatch program

import time

# Display the instructions

print("Press ENTER to begin. Afterwards, press ender to 'click' the stopwatch\nPress CTRL+C to quit")

input() # Press Enter to begin

print("Started")

start_time = time.time()  # Get the start time
last_time = start_time
lap_no = 1

# Start tracking the laptimes
try:

    while True:  # Sets a loop that goes on forever...
        input()  # Waits for the user to hit enter again.
        lap_time = round(time.time() - last_time, 2)
        # When they do, calculate how many seconds have passed for THIS lap - round to 2dp.

        total_time = round(time.time() - start_time, 2)
        # This works out how many seconds have passed IN TOTAL from the start until now.

        print("Lap{}: {} ({})".format(lap_no, total_time, lap_time), end="")

        lap_no += 1  # Increase the lap number by 1.
        last_time = time.time()  # Reset the last lap time.

except KeyboardInterrupt:  # If a Keyboard Interrupt error occurs (use hits CTRL & C) then...
    print("\nDone.")
