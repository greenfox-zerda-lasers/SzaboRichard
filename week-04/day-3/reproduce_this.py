from tkinter import *

def line_cube(x,y,size, offset):

    return canvas.create_rectangle(x+offset, y+offset, x +size+offset, y +size+offset, fill="purple")



root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

for i in range(300 // 20):
    line_cube(0,0,20,20*i)


root.mainloop()
