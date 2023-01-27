import turtle

#1
turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(10)

for step in range(6):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(360 / 3)
    turtle.end_fill()
    turtle.forward(50)
    turtle.right(60)

turtle.hideturtle()

#2
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()