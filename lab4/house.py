# house.py
#
# Created by: R. Givens
# Modified by: Will Schick
#
# Date: 2/27/2018
#
# This program draws a collection of geometric shapes and text on
# graphics canvas to create the appearance of a house.

from ezgraphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow(320, 410)
win.setTitle("This Little House")
canvas = win.canvas()

# Draw on the canvas.
#House Base
canvas.setColor(175,25,25)
canvas.setOutline(0,0,0)
canvas.drawRect(10, 135, 300, 300)
#Door
canvas.setColor(100,0,0)
canvas.drawRect(60, 235, 80, 200)
#Window
canvas.setColor(0,200,255)
canvas.setOutline(0,0,0)
canvas.drawRect(190, 275, 80, 80)
#Window Frames
canvas.setColor(0,0,0)
canvas.drawLine(190, 315, 270, 315)
canvas.drawLine(230, 275, 230, 355)
#Arrow
canvas.setColor(255,255,255)
canvas.drawArrow(75, 265, 125, 265)
#Doorknob
canvas.setColor(255,253,0)
canvas.setOutline(0,0,0)
canvas.drawOval(120, 330, 10, 10)
#Roof
canvas.setColor(50,50,100)
canvas.setOutline(0,0,0)
canvas.drawPoly(10, 135, 160, 10, 310, 135)
#Address
canvas.setColor(0,0,0)
canvas.drawText(150, 265, "1")
canvas.drawText(150, 280, "0")
canvas.drawText(150, 295, "1")

# Wait for the user to close the window.
win.wait()
