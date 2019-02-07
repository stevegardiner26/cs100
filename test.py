import turtle

s = turtle.Screen()
t = turtle.Turtle()

sides = input("How many sides?")

if int(sides) < 3:
    print('Must Enter 3 or Higher!')
else:
    for shape in range(3, int(sides)+1):
        for side in range(shape):
            t.fd(100)
            t.lt(360/shape)

input()
