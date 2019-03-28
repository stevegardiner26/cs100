# Steven Gardiner
# CS 100 2018S Section 004
# HW 11 Dog Class, January 23, 2018


class Dog:

    species = 'canis familiaris'

    # Class Constructor
    def __init__(self, name, breed, tricks=[]):
        self.name = name
        self.breed = breed
        self.tricks = tricks

    def teach(self, trick):
        self.tricks.append(trick)
        print(str(self.name) + ' knows ' + str(trick))

    def knows(self, trick):
        if trick in self.tricks:
            print('Yes, ' + str(self.name) + ' knows ' + str(trick))
            return True
        else:
            print('No, ' + str(self.name) + ' doesn\'t know ' + str(trick))
            return False
