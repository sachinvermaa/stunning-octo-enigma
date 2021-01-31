# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:39:18 2021

@author: sachinverma
"""


import turtle
# from turtle import *

av=turtle.Turtle()
######################
av.speed(8)
######################
window = turtle.getscreen()
window.bgcolor("black")
av.color("grey")
av.up()
av.goto(0,-180)
# av.clear()
av.down()
av.pensize(15)
# av.fd(100)
av.circle(150)
av.up()
av.goto(0,-130)
av.down()
av.circle(100)
av.pensize(1)
av.left(180)
av.circle(-100,extent=110)
av.right(69)
av.fillcolor("grey")
av.color("grey")
av.begin_fill() 
for i in range(0,5):
    print(i)
    av.forward(190)
    av.right(144)
av.end_fill()

av.up()
av.goto(0,-130)
av.down()
# av.right(90)
# av.pensize(1)
av.begin_fill()
av.circle(100,180)
av.end_fill()
av.left(180)
# av.up()
av.begin_fill()
av.fd(35)
av.left(75)
av.fd(45)
av.right(90)
av.circle(-120,28)
av.right(48)
av.fd(80)
av.goto(0,0)
av.end_fill()


av.goto(0,-180)
av.begin_fill()
av.left(90)
av.circle(120,30)
av.left(83)
for i in range(105):
    if i in range(13,30):
        av.fd(1)
        av.right(3)
    else:
        av.fd(1)

av.goto(0,0)
av.goto(0,-180)
av.end_fill()

av.setheading(0)
av.circle(120,30)
av.left(80)
######################
# for i in range(50):
#     if i in range(13,30):
#         av.fd(1)
#         av.right(3)
#     else:
#         av.fd(1)
# av.fd()        
# ######################
# av.fd(5)
av.fillcolor("black")
av.color("black")
av.begin_fill()
for i in range(0,46):
    if i in range(0,16):
        if i in range(0,6):
            av.fd(3)
            av.right(2)
        else:
            av.fd(1)
            av.right(3)
    elif i in range(16,36):
        av.fd(4)
        av.right(1)
    # elif i in range(37,38):
    #     av.fd(1)
        
    else :
        av.fd(1)
        av.left(3)
av.fd(17)
av.right(90)
av.fd(5)    
av.end_fill()    
# for i in range(97):
#     av.undo()


av.up()  
av.goto(0,-120)   
av.setheading(90)
av.pensize(5)
# av.fd(5)
av.color("black")
av.down()
av.fd(90)
av.left(107)
av.fd(60)
av.goto(0,-30)
av.right(72)
av.fd(60)
av.goto(0,-30)
av.setheading(0)
av.pensize(1)

av.begin_fill()
av.fd(27)
av.left(15)
av.fd(65)
av.right(83)
av.fd(11)
av.left(105)
av.fd(21)
av.right(90)
av.fd(5)
av.right(90)
av.fd(42)
av.right(8)
for i in range(25):
    if i in range(0,10):
        av.fd(1)
        av.right(2)
    else:
        av.fd(3)
        av.right(2)
av.right(75)
av.fd(6)             
av.left(95)
av.fd(27)
av.end_fill()
av.up()
av.goto(0,-145)
av.setheading(0)
av.down()
av.pensize(8)
av.fd(32)
av.right(45)
av.fd(12)
av.left(90)
av.fd(25)

av.up()
av.pensize(1)
av.setheading(0)
av.goto(0,-171)
av.begin_fill()
av.down()
av.goto(0,-163)
av.fd(8)
av.right(45)
av.forward(5)
av.left(38)
av.fd(11)
av.end_fill()
# for i in range(10):
#     av.undo()
av.up()
av.fd(50)