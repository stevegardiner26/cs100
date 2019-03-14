'''
Steven Gardiner
CS 100 2018S Section 004
HW 09, March 14, 2018
'''

# Problem 2

def file_stats(in_file):
    # Open the in file
    file = open(in_file, 'r')
    # Read the file by line
    lines = file.readlines()
    # Declare the count of the words and chars
    words = 0
    chars = 0
    # looping through the lines
    for line in lines:
        # Adding the words and chars to the counting variable
        words += len(line.split(' '))
        chars += len(line)

    # Print all the data
    print('Lines: ' + str(len(lines)))
    print('Words: ' + str(words))
    print('Characters: ' + str(chars))
    # Close the file
    file.close()
    return

