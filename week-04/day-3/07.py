from tkinter import *
# create a 300x300 canvas.
# fill it with four different size and color rectangles.

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

color= ["blue", "red", "yellow", "brown", "orange"]

for i in range(5):
    box = canvas.create_rectangle(150+i*2,100+i,120+3*i, 50+i*5, fill=color[i])

root.mainloop()
