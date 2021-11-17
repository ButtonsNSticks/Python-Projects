spam = ["apples","bannanas","tofu",6]

def makestring (listvalue):
    mystring=""
    for item in range(len(listvalue)-1): # For loop that will run through all of the list items BAR the last one
        mystring += str(listvalue[item]) + ", "

    mystring += "and " + str(listvalue[-1])

    return mystring

print(makestring(spam))
