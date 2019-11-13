
#function file

import turtle
bob=turtle.Turtle()

#function
def polygon(sides,distance,color):
    bob.color(color)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def star (d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range (5):
        bob.forward(d)
        bob.right(144)
    bob.end_fill()

def jump (x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def explosion (d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()

def sun (d):
    bob.begin_fill()
    bob.circle(d)
    bob.end_fill()

def mountain (x,y,color):
    jump(x,y)
    bob.begin_fill()
    bob.color(color)
    bob.circle(180)
    bob.end_fill()
    


            
    
    
