from tkinter import *
# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def line_drawer(x,y):
    coordx = x
    coordy = y

    root = Tk()
    canvas = Canvas(root, width="300", height="300")
    canvas.pack()

    line1 = canvas.create_line(150, 150, coordx, coordy)
    # line2 = canvas.create_line(coordx, coordy, 150, 150)

    root.mainloop()

line_drawer(30, 30)
line_drawer(80, 100)
line_drawer(100, 300)
