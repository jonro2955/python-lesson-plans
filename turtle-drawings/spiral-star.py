from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(0)
screen = Screen()

R = 255
G = 0
B = 0

screen.bgcolor((255, 255, 255))

for i in range(255):
    G += 1
    B += 1
    R -= 1
    turtle.color((R, G, B))
    turtle.forward(i*2)
    turtle.right(98)
    print(i)

screen.exitonclick()