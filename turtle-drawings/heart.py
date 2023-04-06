import turtle

t = turtle.Turtle()
wn = turtle.Screen()
t.speed(0)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.left(45)


def curve(times, line, angle):
    for i in range(times):
        t.forward(line)
        t.right(angle)


curve(32, 6, 4)
curve(30, 9, 3)
t.right(15)
curve(30, 9, 3)
curve(32, 6, 4)


wn.exitonclick()

