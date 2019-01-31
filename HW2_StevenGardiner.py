"""
Steven Gardiner
CS 100 2018S Section 004
HW 02, January 24, 2018
"""

# Question 1

# Initialized the grades list
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

# Initialized the frequency list
frequency = []
# Counts amount of provided letter in the grades list and adds it to the frequency list
frequency.append(grades.count('A'))
frequency.append(grades.count('B'))
frequency.append(grades.count('C'))
frequency.append(grades.count('D'))
frequency.append(grades.count('F'))\

# Prints the Frequency List
print(frequency)

# Question 2

# 2a (Initialized a list called dog_breeds with the given values
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print(dog_breeds)

# 2b Use slicing to create a list callled herding_dogs that takes only the first two elements of dog_breeds
herding_dogs = dog_breeds[0:2]
print(herding_dogs)

# 2c Use indexing to create a lits tiny_dogs that takes only the last two elements of dog_breeds
tiny_dogs = [dog_breeds[len(dog_breeds)-2], dog_breeds[len(dog_breeds)-1]]
print(tiny_dogs)

# Im not sure exactly how this was required to be done so I did it another way
tiny_dogs = []
tiny_dogs.insert(-1, dog_breeds.pop(-1))
tiny_dogs.insert(-1, dog_breeds.pop(-1))
print(tiny_dogs)

# 2d Test whether 'Persian' is within the list dog_breeds and prints the value true or false
print(bool(dog_breeds.count('Persian')))
