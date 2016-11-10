from tkinter import *
# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def square_drawSize(param, width, height):
    param = param / 2
    return canvas.create_rectangle(width/2 - param, height/2 - param, width/2 + param, height/2 + param, fill="blue")


root = Tk()

width = 300
height = 300
canvas = Canvas(root, width=width, height=height)
canvas.pack()

square_drawSize(70,300,300)

root.mainloop()
