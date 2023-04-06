import turtle

wn = turtle.Screen()
wn.bgcolor("purple")
t = turtle.Turtle()
t.speed(5)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.color("black", "red")
t.begin_fill()
t.circle(80)
t.end_fill()

turtle.done()
