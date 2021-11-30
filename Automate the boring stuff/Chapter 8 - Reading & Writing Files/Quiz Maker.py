#! python3
# This makes quizzes with questions & answers in random order, along with the answer key.

import random  # Allows for the generation of random numbers.

# The quiz data. Stored as a dictionary.  Keys are states and values are their capitals.

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}

# Generate 35 quiz files

for quiznum in range(35):  # Will loop 35 times, from 0 to 34.

    # Create the quiz and answer key files

    quizfile = open("capitalsquiz%s.txt" % (quiznum + 1), "w")
    # This uses string formatting.
    # The %s is a placeholder that will be swapped out for the value of the variable (quiznum +1)
    # If python cannot find the file it is asked to open, it will make it.
    # So this will create the files 1st and open them in WRITE mode.

    answerkeyfile = open("capitalsquiz_answers%s.txt" % (quiznum + 1), "w")  # Same as above but for the answers.

    # Write out the header for the quiz
    quizfile.write("Name\n\nDate:\n\nPeriod:\n\n")
    quizfile.write((" " * 20) + "State Capitals Quiz (Form %s)" % (quiznum + 1))
    quizfile.write("\n\n")

    # Shuffle the order of the states.

    states = list(capitals.keys())  # Makes a list from the keys, which in this case are the different states of USA.
    random.shuffle(states)  # Shuffles the list into a random order.

    # Loop through all 50 states, making a question for each.

    for questionnum in range(50):  # A loop that will make 50 questions

        # Get right and wrong answers

        correctanswer = capitals[states[questionnum]]
        # This 1st looks up the nth state stored in the states list, so on 1st loop will find state 0
        # It then takes the name of this state found in states[quesionnum] and passes the name of the state
        # to the capitals dictionary. As this state is the "key" captials[State name] will return the name
        # of the capital city for the state in question. This is stored in correctanswer variable.

        wronganswers = list(capitals.values())
        # Makes a list of ALL the values in the capitals dictionary
        # In this case these are the names of the capital cities.

        del wronganswers[wronganswers.index(correctanswer)]
        # correctanswer will hold the name of the capital city which is the answer to the question.
        # wronganswers.index(correctanswer) will find the mention of the capital city in the wronganswers list
        # and return it's postion in the wronganswers list, ie [0] or [20] or whatever
        # del wronganswers[position] will then remove the capital city from the list, leaving only wrong answers.

        wronganswers = random.sample(wronganswers, 3)  # Takes 3 items at random from the list of wrong answers.

        answeroptions = wronganswers + [correctanswer]
        # Makes a new list that has the 3 wrong answers + the correct one

        random.shuffle(answeroptions)  # Shuffles the 4 cities in the list.

        # Write the question & answer options to the quiz file.

        quizfile.write("%s. What is the capital of %s?\n\n" % (questionnum + 1, states[questionnum]))

        # This will write a line to the text file.
        # The first %s will be replaced with questionnum+1
        # The second %s will be replaced with states[questionnum]
        # states[questionnum] will return the name of the state in position X

        for i in range(4):  # Sets up a loop that will run 4 times -> 0 to 3.

            quizfile.write(" %s. %s\n" % ("ABCD"[i], answeroptions[i]))
            # The "ABCD" is treated as a list and so when i is 0 it will pick A and print it in the 1st %s.
            # When i = 1 it will pick B and so on.
            # Similarly for the 2nd % it will replace this with the entry in answeroptions list in postion i.

            quizfile.write("\n")

            # Write the answer kry to a file
            answerkeyfile.write(" %s. %s\n" % (questionnum + 1, "ABCD"[answeroptions.index(correctanswer)]))
            # This will write the answer to the answerkeyfile.
            # The 1st substitution is the question number (1 to 50)
            # The 2nd substitution again treats "ABCD" as a list and will pick the letter whose position
            # Matches the number given by the position of the correct answer in the answeroptions list.

    quizfile.close()  # Close the quiz file.
    answerkeyfile.close()  # Close the answer file.
