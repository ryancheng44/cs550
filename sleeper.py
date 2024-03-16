'''
Ryan Cheng
10/19/23
Sources: None
Reflection: This was definitely quite a fun assignment. Being able to have two turtles simultaneously was
            a game changer. That made the assignment a lot easier. Also had to download and install the
            newest version of Python since the built-in macOS version didn't support turtle.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import turtle

def recurse(right_turtle, length, pos, heading):
    if length <= 0:
        return

    right_turtle.right(20)
    right_turtle.forward(length * 20)
    left_turtle = turtle.Turtle()
    left_turtle.up()
    left_turtle.setpos(pos)
    left_turtle.setheading(heading + 20)
    left_turtle.down()
    left_turtle.forward(length * 20)
    
    recurse(right_turtle, length - 1, right_turtle.pos(), right_turtle.heading())
    recurse(left_turtle, length - 1, left_turtle.pos(), left_turtle.heading())

right_turtle = turtle.Turtle()

right_turtle.up()
right_turtle.setpos(0, -200)
right_turtle.down()

right_turtle.setheading(90)
right_turtle.forward(100)

recurse(right_turtle, 5, right_turtle.pos(), right_turtle.heading())

turtle.exitonclick()