from tkinter import *
# Recreate this triangle fractal:

root = Tk()
canvas = Canvas(root, width="500", height="500")
canvas.pack()
height_ratio = 3**.5/2

def triangle_draw(x,y,size):

     canvas.create_polygon(
        x, y,
        x+size, y,
        x+size/2, y+height_ratio*size,
        outline='green',
        fill = "white"
    )


def draw_stuff(x, y, size):
    triangle_draw(x, y, size)

def draw_recursive(x, y, size):
    if size < 10:
        return
    else:
        draw_stuff(x, y, size)
        # draw_recursive(x, y, size/3)
        draw_recursive(x, y, size/2)
        draw_recursive(x+size/2, y, size/2)
        draw_recursive(x+size/4, y+size*height_ratio/2, size/2)
        # draw_recursive(x+size/3, y+size*2/3, size/3)

draw_recursive(10, 10, 480)


root.mainloop()
