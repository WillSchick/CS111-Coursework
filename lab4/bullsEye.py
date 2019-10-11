# bullsEye.py
#
# Created by: Will Schick
#
# Date: 2/27/2018
#
# This program asks for the size of the window and draws a target and bulls eye to accommodate

from ezgraphics import GraphicsWindow

#UserInput
print("---" *5)
canvasSize = int(input("Target Size?: "))

#Constants & Variables


# Create the window and access the canvas.
win = GraphicsWindow(canvasSize, canvasSize)
canvas = win.canvas()
win.setTitle("Bull's-Eye")

# Draw on the canvas.
#Canvas Color
canvas.setColor("grey")
canvas.drawRect(0,0,canvasSize,canvasSize)

#First Ring
canvas.setColor("black")
canvas.drawOval(0,0,canvasSize,canvasSize)

#Second Ring
canvas.setColor("white")
canvas.drawOval(canvasSize*.1,canvasSize*.1,canvasSize*.80,canvasSize*.80)

#Third Ring
canvas.setColor("black")
canvas.drawOval(canvasSize*.2,canvasSize*.2,canvasSize*.60,canvasSize*.60)

#Fourth Ring
canvas.setColor("white")
canvas.drawOval(canvasSize*.3,canvasSize*.3,canvasSize*.40,canvasSize*.40)

#Bull's-Eye Ring
canvas.setColor("red")
canvas.drawOval(canvasSize*.4,canvasSize*.4,canvasSize*.20,canvasSize*.20)




# Wait
win.wait()
