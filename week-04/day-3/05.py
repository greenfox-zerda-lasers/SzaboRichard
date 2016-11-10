from tkinter import *
# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def line_drawing(x,y):
    return canvas.create_line(x,y,x+50,y)



root = Tk()
canvas = Canvas(root, width="300", height="300")
canvas.pack()


line_drawing(50, 60)
line_drawing(150, 250)
line_drawing(180, 100)

root.mainloop()
