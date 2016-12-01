from tkinter import *
from PIL import Image, ImageTk
import random

class GameView:
    def __init__(self):
        self.tile = 72
        self.root = Tk()
        self.canvas = Canvas(self.root, width =12*self.tile, height = 11*self.tile)
        
        self.canvas.pack()


    def map_drawer(self, maplist):
        for row in range(len(maplist):
            for column in range(len(row)):
                if maplist[row][column] == 0:
                    self.canvas.create_image(column*self.tile, row.*self.tile, image = )
