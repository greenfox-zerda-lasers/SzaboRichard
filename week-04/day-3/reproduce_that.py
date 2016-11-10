from tkinter import *

def greater_cube(x,y,size):
    return canvas.create_rectangle(x,y,x+size,y+size, fill="purple")

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()
offset = 0
for i in range(5):
    greater_cube(offset, offset, i*20)
    offset += i*20

root.mainloop()
