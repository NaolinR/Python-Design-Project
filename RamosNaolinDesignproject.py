from RamosFunctions import*
turtle.colormode(255)
bob.speed(0)

#background
bob.width(50)
bob.speed(0)
x=-460
y=400
jump(x,y)
for times in range (256):
    c=(255, 178, times)
    bob.color(c)
    bob.forward(1000)
    jump (x,y-times*3)

#sun
jump(20,80)
bob.color(255,255,204)
bob.begin_fill()
sun(120)
bob.end_fill()
bob.width(2)
for times in range (100):
    bob.begin_fill()
    c=(255,255,255-times)
    bob.color(c)
    bob.circle(135-times)
    bob.end_fill()

jump(-180,120)
bob.color(255,255,204)
for times in range(20):
    bob.circle(50-times*2)
    bob.left(72)
    bob.forward(10)

jump(250,120)
for times in range(20):
    bob.circle(50-times*2)
    bob.left(72)
    bob.forward(10)
    
jump(30,100)
for times in range(20):
    bob.circle(50-times)
    bob.right(52)
    
#mountains
mountain(-200,-380,(255,229,204))
mountain(420,-380,(255,229,204))
mountain(350,-480,"gray")
mountain(200,-480,"gray")
mountain(50,-480,"gray")
mountain(-100,-480,"gray")
mountain(-250,-480,"gray")
mountain(-400,-480,"gray")
mountain(500,-480,"gray")
mountain(-400,-580,"black")
mountain(-250,-580,"black")
mountain(-100,-580,"black")
mountain(50,-580,"black")
mountain(200,-580,"black")
mountain(350,-550,"black")
mountain(500,-580,"black")
    


