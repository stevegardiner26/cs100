# Steven Gardiner
# CS 100 2018S Section 004
# HW 03, February 7, 2018

import turtle
import math

# Question 1
s = turtle.Screen()
t = turtle.Turtle()

t.fd(100)
t.lt(360/3)
t.fd(100)
t.lt(360/3)
t.fd(100)
t.lt(360/3)
t.fd(100)
t.lt(360/4)
t.fd(100)
t.lt(360/4)
t.fd(100)
t.lt(360/4)
t.fd(100)
t.lt(360/4)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)

# Question 2

t.circle(50)
t.penup()
t.rt(90)
t.fd(50)
t.lt(90)
t.pendown()
t.circle(100)
t.penup()
t.rt(90)
t.fd(50)
t.lt(90)
t.pendown()
t.circle(150)
t.penup()
t.rt(90)
t.fd(50)
t.lt(90)
t.pendown()
t.circle(200)

# Question 3
# Part A

print(math.factorial(100))

# Part B

print(math.log(1000000, 2))

# Part C

print(math.gcd(63, 49))

input()
