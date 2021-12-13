import logging
import random

logging.disable()

# Configure Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

# Set up variables

guess = ""  # Sets up empty string
attempts = 2

# Toss the coin
toss = random.randint(0, 1)  # Makes a random integer 0 or 1. 0 is tails. 1 is heads.
logging.debug(toss)

for attempt in range(attempts):

    while str.lower(guess) not in ("heads", "tails"):

        # Makes a TUPLE
        # This sets up a loop that will go around if the guess isn't either heads or tails
        # Added in .lower to force the case else HEADS or Heads won't match

        print("Guess the coin toss! Enter heads or tails:")
        logging.debug("Player guess %s" % str.lower(guess))
        guess = str.lower(input())  # Asks the player for input, forces it lowercase

    # We now have the player's guess
    # Let's convert the string into the corresponding numbers, 0 for tails, 1 for heads.

    if guess == "heads":
        guess = 1

    if guess == "tails":
        guess = 0

    # Now lets check to see if the player's guess matches the actual coin toss

    if toss == guess:
        print("You got it!")
        exit()  # Player got it right, lets end the code

    elif attempt < 1:
        print("No, try again")
        guess = ""
        # Player got it wrong, clear the guess
        # Contine ?

    else:
        print("Nope, you suck at this game!")

