'''
Steven Gardiner
CS 100 2018S Section 004
HW 09, March 14, 2018
'''

# Problem 3

# Importing the string for string.punctuation
import string


def repeat_words(in_file, out_file):
    # Opening the file to read the lines
    file = open(in_file, 'r')
    # Adding each line as an element of an List
    lines = file.readlines()
    # Closing the read file
    file.close()
    # Opening the write file
    writer = open(out_file, 'w')
    # Declaring temp line and write line variables
    write_line = ''
    temp_line = []
    # Looping through each of the lines in the content
    for line in lines:
        # Making the line lowercase
        line = line.lower()
        # Removing Punctuation from the line
        exclude = set(string.punctuation)
        line = ''.join(ch for ch in line if ch not in exclude)
        # Splitting the line into an array of words
        words = line.split(' ')
        # Looping through the words in the wordList
        for word in words:
            # Checking if the word was in the line before the current word and if it wasn't it adds it to the temp_line
            if word not in temp_line:
                temp_line.append(word)
            # if the word was in the line before it goes through one final check to see if it is already been added to the output aka write_line
            else:
                if word not in write_line.split(' '):
                    # adding the word to write)line
                    write_line += ' ' + word
        # Adding a Line Break to the write_line so each line is a new line
        write_line += '\n'
        # Writing the write_line to the write file
        writer.write(write_line)
        # Reseting the temp values per line
        write_line = ''
        temp_line = []
    # Closing the Write File
    writer.close()
    return
