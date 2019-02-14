# Steven Gardiner
# CS 100 2018S Section 004
# HW 04, February 14, 2018
import turtle

# Question 1

# 1a
a = 3
b = 4
c = 5

# 1b
if a < b:
    print("OK")

# 1c
if c < b:
    print("OK")

# 1d
if (a+b) == c:
    print("OK")

# 1e
if (a**2 + b**2) == c**2:
    print("OK")

# Question 2

# 2a
a = 3
b = 4
c = 5

# 2b
if a < b:
    print("OK")
else:
    print("NOT OK")

# 2c
if c < b:
    print("OK")
else:
    print("NOT OK")

# 2d
if (a+b) == c:
    print("OK")
else:
    print("NOT OK")

# 2e
if (a**2 + b**2) == c**2:
    print("OK")
else:
    print("NOT OK")

# Question 3

color = input("What color?")
width = int(input("What line width?"))
length = int(input("What line length?"))
shape = input("line, triangle or square?")

s = turtle.Screen()
t = turtle.Turtle()

t.color(color)
t.width(width)

if shape == "line":
    t.fd(length)
elif shape == "triangle":
    t.rt(360/3)
    t.fd(length)
    t.rt(360/3)
    t.fd(length)
    t.rt(360/3)
    t.fd(length)
elif shape == "square":
    t.fd(length)
    t.rt(360/4)
    t.fd(length)
    t.rt(360/4)
    t.fd(length)
    t.rt(360/4)
    t.fd(length)
    t.rt(360/4)

input("This is here so you can see the turtle")
