import turtle
import random
bob=turtle.Screen()
bobby=turtle.Turtle()
bobby.shape("turtle")
bob.colormode(255)
bobby.speed(0)
bobby.turtlesize(2)
Quit=0
while Quit==0:
    bobby.penup()
    bobby.goto(random.randint(-200,200),random.randint(-200,200))
    bobby.pendown()
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    bobby.color((r,g,b))
    cheese =0
    sides = int(bob.numinput("sides","How many sides does your shape have?"))
    angle = 360/sides
    distance = 300/(sides/2)
    bobby.begin_fill()
    while cheese < sides:
        bobby.forward(distance)
        bobby.right(angle)
        cheese += 1
    bobby.end_fill()
    Answer=bob.textinput("Quit?","Type \"QUIT\" to close.")
    if Answer=="QUIT":
        Quit=1
        continue
    else:
        Quit=0
turtle.Screen().exitonclick()