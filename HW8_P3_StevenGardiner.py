# Steven Gardiner
# CS 100 2018S Section 004
# HW 08, March 7, 2018
# Problem 3


def enter_new_password():
    password = ''
    has_digit = False
    while not 8 <= len(password) <= 15 or has_digit == False:
        password = input("Enter a New Password: ")
        if not 8 <= len(password) <= 15:
            print("You must enter a password from 8-15 characters!")
        for letter in password:
            if letter.isdigit():
                has_digit = True
        if has_digit == False:
            print("You must have a digit in the password")
    

enter_new_password()
