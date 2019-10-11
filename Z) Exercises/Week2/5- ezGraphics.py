#ezGraphics.py
#
#Will Schick
#
#2/26/2018
#
#Testing and Learning graphics in Python
#Drawing methods

#Import the Module
from ezgraphics import *

#Constants and Variables
win = GraphicsWindow(400,400)
canvas = win.canvas()

#Window Setup
win.setTitle("Title")

#Computation

#- Draw
#canvas.drawLine(0,0,400,400)
#canvas.drawLine(400,0,0,400)
#canvas.drawRect(100,100,200,200)
canvas.drawOval(100,100,200,200)
#canvas.drawPoly(100,100,200,100,150,150)

canvas.drawText(175,190,"Hot damn")
canvas.setTextFont("helvetica","bold",20)
canvas.drawText(140,140,"HOT DAMN")

#- Wait
win.wait()

#Printing