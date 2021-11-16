def collatz(number):
    if number % 2 == 0:  # Number is even
        x = number // 2

    if number % 2 == 1:  # Number is odd.
        x = (3 * number) + 1

    print(x)
    return x

isnumber = False

while isnumber == False:

    try:
        startnum = int(input("Please type in a whole number: "))
        isnumber = True

    except ValueError:
        print("That was not an integer, please try again!")

# Ask user to type in a whole number, convert to integer just to be sure

output = collatz(startnum)

while output != 1:
    output = collatz(output)
