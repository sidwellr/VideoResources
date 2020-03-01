# Draw a Koch snowflake

import turtle

def curve(dist, order):
    if order > 0:
        for theta in [60, -120, 60, 0]:
            curve(dist/3, order-1)
            turtle.left(theta)
    else:
        turtle.forward(dist)

def snowflake(dist, order):
    curve(dist, order)
    turtle.right(120)
    curve(dist, order)
    turtle.right(120)
    curve(dist, order)
    turtle.right(120)

# Test
turtle.reset()
turtle.setup(1920, 1080)
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-800,-200)
turtle.pendown()
turtle.width(3)
curve(1600,6)
