# Steven Gardiner
# CS 100 2018S Section 004
# HW 08, March 7, 2018
# Problem 4

import random

rando = random.randint(0, 50)
guess = ''
incorrect = 0
currTry = 0
print("I am thinking of a number between 0-50. You have 5 tries to guess it!")
while rando:
    if incorrect == 5:
        print("You ran out of tries, the number was: " + str(rando))
        break
    else:
        currTry += 1
        guess = input("Guess(" + str(currTry) + ")?: ")
        guess = int(guess)
        if guess == rando:
            print("Congrats you guessed correctly!")
            break
        elif guess > rando:
            print("You guessed too high try again: ")
            incorrect += 1
        elif guess < rando:
            print("You guessed too low try again: ")
            incorrect += 1

