from tkinter import *
# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

def square_drawSize(param):
    param = param / 2
    return canvas.create_rectangle(width/2 - param, height/2 - param, width/2 + param, height/2 + param, fill="blue")


root = Tk()
width = 300
height = 300
canvas = Canvas(root, width=width, height=height)
canvas.pack()

for i in range(20,0,-1):
    square_drawSize(70+5*i)


root.mainloop()
