from tkinter import *
# create a 300x300 canvas.
# fill it with a checkerboard pattern.

def chessboard():
    color = "black"
    k = 300 // 8
    for j in range(8) :
        for i in range(8):
            if i % 2 == 0 and j % 2 == 1 or j % 2 == 0 and i % 2 == 1:
                color = "black"
            else:
                color = "white"
            canvas.create_rectangle(i*k,j*k, k+i*k, k+j*k, fill=color)

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

chessboard()

root.mainloop()
