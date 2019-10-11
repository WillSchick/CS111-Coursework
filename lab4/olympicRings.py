# olympicRings.py
#
# Created by: Will Schick
#
# Date: 2/27/2018
#
# This program draws the olympic rings in a graphics window

from ezgraphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow(340, 160)
canvas = win.canvas()
win.setTitle("Olympic Rings!")

# Draw on the canvas.
#Blue Ring
canvas.setOutline("blue")
canvas.drawOval(0, 0, 100, 100)

#Yellow Ring
canvas.setOutline("yellow")
canvas.drawOval(60, 60, 100, 100)

#Black Ring
canvas.setOutline("black")
canvas.drawOval(120, 0, 100, 100)

#Green Ring
canvas.setOutline("green")
canvas.drawOval(180, 60, 100, 100)

#Red Ring
canvas.setOutline("red")
canvas.drawOval(240, 0, 100, 100)


# Wait
win.wait()
