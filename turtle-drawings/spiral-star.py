from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(0)
screen = Screen()
screen.colormode(255)

R = 255
G = 0
B = 0

for i in range(255):
    G += 1
    B += 1
    R -= 1
    turtle.pencolor(R, G, B)
    turtle.forward(i * 2)
    turtle.right(98)

screen.exitonclick()
