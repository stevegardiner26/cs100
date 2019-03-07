# Steven Gardiner
# CS 100 2018S Section 004
# HW 08, February 14, 2018
# Problem 1

def twoWords(length, firstLetter):
    word = ''
    while len(word) != length:
        word = input("Enter a " + str(length) + " Letter Word: ")

    output.append(word)
    word2 = ''
    while word2[0] != firstLetter.lower() or word2[0] != firstLetter.upper():
        word2 = input("Enter a word starting with " + firstLetter)


twoWords(4, "B")