from tkinter import *
# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def square_draw(param, param2):

    x = param
    y = param2

    root = Tk()

    canvas = Canvas(root, width="300", height="300")
    canvas.pack()

    box = canvas.create_rectangle(50,50, param, param2)

    root.mainloop()

square_draw(70,55)
square_draw(120,100)
square_draw(150,100)
