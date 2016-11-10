from tkinter import *
# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def draw_draw(param, color):

    return canvas.create_rectangle(width/2 - param, height/2 - param, width/2 + param, height/2 + param, fill=color )


root = Tk()
width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet",]

for i in range(7,0, -1):
    draw_draw(80+i*5, rainbow.pop())

root.mainloop()
