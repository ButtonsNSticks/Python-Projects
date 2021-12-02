# Import modules

# Open text file

filename = "textfile.txt"  # The name of the text file that will be read.
the_text = open(filename, "r")  # Opens the file as READ ONLY

# Todo: Print the contents of the text file
the_text_content = the_text.read()  # Put the contents of the text file into the variable as a STRING.
print(the_text_content+"\n")  # Print the contents of the text file on the screen.


# Todo: Put the text file into a list.

word_list = the_text_content.split(" ")
# We split the contents of the file up and put each word as an entry into a LIST.

# print(word_list)  # Uncomment to print the list.

# Todo: Loop through the list

for word_position in range(len(word_list)):  # Loop over the items in the list by their INDEX numbers (position)

    if "ADJECTIVE" in word_list[word_position]:   # If we find the word ADJECTIVE in caps...
        replacement = input("Enter an adjective: ")  # Ask the user to replace it.
        word_swap = word_list[word_position].replace("ADJECTIVE", replacement)
        word_list[word_position] = word_swap  # Replace the ADJECTIVE with what was typed.

    elif "NOUN" in word_list[word_position]:   # If we find the word NOUN in caps...
        replacement = input("Enter an noun: ")  # ...ask the user to replace it...
        word_swap = word_list[word_position].replace("NOUN", replacement)
        word_list[word_position] = word_swap  # Replace the NOUN with what was typed.

    elif "ADVERB" in word_list[word_position]:   # If we find the word ADVERB in caps...
        replacement = input("Enter an adverb: ")  # ...ask the user to replace it...
        word_swap = word_list[word_position].replace("ADVERB", replacement)
        word_list[word_position] = word_swap  # Replace the ADVERB with what was typed.

    elif "VERB" in word_list[word_position]:   # If we find the word VERB in caps...
        replacement = input("Enter an verb: ")  # ...ask the user to replace it...
        word_swap = word_list[word_position].replace("VERB", replacement)
        word_list[word_position] = word_swap  # Replace the VERB with what was typed.

# Todo: Turn the list back into a string

new_text = " ".join(word_list)

# Todo: Save the string into a new text file.

new_file = open("newfile.txt", "w")
new_file.write(new_text)
new_file.close()
