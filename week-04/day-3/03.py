from tkinter import *
# create a 300x300 canvas.
# draw its diagonals in green.

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

diagonal = canvas.create_line(0, 0, 300, 300, fill="green")
diagonal2 = canvas.create_line(0,300, 300, 0, fill="green")

root.mainloop()
