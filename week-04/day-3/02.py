from tkinter import *
# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.


root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

line1 = canvas.create_line(150, 150, 150, 55, fill="red")
line2 = canvas.create_line(150, 55, 50, 55, fill="yellow" )
line3 = canvas.create_line(150,150,50, 150, fill="blue")
line4 = canvas.create_line(50, 55, 50, 150, fill="orange" )

root.mainloop()
