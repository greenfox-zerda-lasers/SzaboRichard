from tkinter import *
# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

root = Tk()
canvas = Canvas(root, width="300", height="300")
canvas.pack()

line1 = canvas.create_line(0,150, 300, 150, fill="green")
line2 = canvas.create_line(150, 0, 150, 300, fill="red")

root.mainloop()
