# This is the guess the number game which is at the end of Chapter 3 of the book.
# I've added in some extra comments to explain what's going on.

import random  # Imports the random module so we can generate random numbers.

secretnumber = random.randint(1, 20)  # Calls the random integer function from imported random module.
# Generates a whole number between 1 and 20 & sets it to the variable secretnumber.

print("I am thinking of a number between 1 & 20")

# Ask the player to guess 6 times

for guessestaken in range(1, 7):  # Sets up a FOR loop that will run 6 times: 1,2,3,4,5,6 (stops at 7).

    print("Take a guess: ")
    guess = int(input())  # Ask the user to type in a number and convert it to a INTEGER data type.

    if guess < secretnumber:
        print("Your guess is too low!")
    elif guess > secretnumber:
        print("Your guess is too high!")
    else:
        break  # The player guessed the right number & we want to exit the loop.

if guess == secretnumber:
    print("Well Done! You guessed the number in", str(guessestaken), "attempts")
else:
    print("Nope, the number I was think of was:", str(secretnumber))
