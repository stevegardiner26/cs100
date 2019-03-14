'''
Steven Gardiner
CS 100 2018S Section 004
HW 10, March 14, 2018
'''

# Problem 1


def initial_letter_count(wordList):
    # Initializing the Dictionary
    d = {}
    # Looping through the words in the list
    for word in wordList:
        # Resetting the count of words starting with that letter to 0
        count = 0
        # Looping through the words again to compare
        for word2 in wordList:
            # Comparing the current words first letter to all of the other word's first letters in the wordList
            if word[0] == word2[0]:
                # if they have the same first letter 1 is added to the count
                count += 1
        # This creates a dictionary key, value pair based off the word's first letter and the count
        d[word[0] + ''] = count
    # Returns the dictionary
    return d


horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initial_letter_count(horton))

