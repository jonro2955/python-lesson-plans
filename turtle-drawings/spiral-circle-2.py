import turtle
import random

t = turtle.Turtle()
t.speed(0)
s = turtle.Screen().bgcolor('black')
colors = ['red', 'magenta', 'blue',
          'cyan', 'green', 'white',
          'yellow']

for i in range(360):
    t.color(random.choice(colors))
    t.left(1)
    t.forward(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
