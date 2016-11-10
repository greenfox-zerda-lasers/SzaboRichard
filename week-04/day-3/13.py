from tkinter import *
# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def funct_13(x,y):

    return canvas.create_line(x,y,x,y, fill="green")


root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

nov = 0
for i in range(10):
    funct_13(20+i*5 / (i-1), 20+i*5 / (i-1))
    # nov +=2
root.mainloop()
