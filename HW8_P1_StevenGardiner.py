# Steven Gardiner
# CS 100 2018S Section 004
# HW 08, March 7, 2018
# Problem 1


def two_words(length, first_letter):
    output = []
    word = ''
    while len(word) != length:
        word = input("Enter a " + str(length) + " Letter Word: ")

    output.append(word)
    word2 = " "
    while word2 != first_letter:
        if word2[0] == first_letter.upper() and word2[0] == first_letter.lower():
            break
        word2 = input("Enter a word starting with " + first_letter + ": ")

    output.append(word2)
    print(output)


two_words(4, "B")
