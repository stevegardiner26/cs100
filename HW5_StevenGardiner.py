# Steven Gardiner
# CS 100 2018S Section 004
# HW 05, February 14, 2018


# Question 1

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    if month[0] == 'J':
        print(month)

# Question 2

for num in range(0, 100):
    if (num % 2 == 0) or (num % 5 == 0):
        print(num)

# Question 3

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)
