'''
Steven Gardiner
CS 100 2018S Section 004
HW 10, March 14, 2018
'''

# Problem 2


def initial_letters(wordList):
    # Initializing the Dictionary
    d = {}
    # Looping through the words in the list
    for word in wordList:
        # Resetting the list of words starting with that letter to an empty list
        list = []
        # Looping through the words again to compare
        for word2 in wordList:
            # Comparing the current words first letter to all of the other word's first letters in the wordList
            if word[0] == word2[0]:
                # if they have the same first letter that word is added to the list
                # Also checking if the word is already in the list to prevent duplicate words
                if word2 not in list:
                    list.append(word2)
        # This creates a dictionary key, value pair based off the word's first letter and the list
        d[word[0] + ''] = list
    # Returns the dictionary
    return d


horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initial_letters(horton))
