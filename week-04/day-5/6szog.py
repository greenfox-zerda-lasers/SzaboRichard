from tkinter import *

root = Tk()
canvas = Canvas(root, width="500", height="500")
canvas.pack()
height_ratio = 3**.5/2

def draw_triangle(x,y, size):
    canvas.create_polygon(
       x, y,
       x+size, y,
       x+size/2, y+height_ratio*size,
       outline='green',
       fill = "white"
   )

def draw(x,y, size):
    draw_triangle(x,y,size)

def draw_rec(x,y, size):
    if size < 10:
        return
    else:
        draw(x,y,size)
        draw_rec(x,y,size/2)
        # draw_rec()

draw_rec(70,70, 100)
draw_rec(120,155,100)
draw_rec(20,155, 100)

root.mainloop()
