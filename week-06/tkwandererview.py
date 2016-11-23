from tkinter import *
from PIL import Image, ImageTk

class GameMap:
    def __init__(self):
        self.tile = 72
        self.root = Tk()
        self.canvas = Canvas(self.root,width= 11*72, height= 11*72)
        self.canvas.pack()
        self.floorimage = PhotoImage(file = "./floor.png")
        self.wallimage = PhotoImage(file = "./wall.png")
        self.bossimage = PhotoImage(file = "./boss.png")
        self.skeleton = PhotoImage(file = "./skeleton.png")
        self.characters = { "hero" : None, "boss" : None, "skeletons" : []}
        self.hero_images = { "down": PhotoImage(file = "./hero-down.png"), "up" : PhotoImage(file = "./hero-up.png"), "left" : PhotoImage(file = "./hero-left.png"), "right" : PhotoImage(file = "./hero-right.png")}


    def draw_map(self, maplist):
        for row in range(len(maplist)):
            for column in range(len(maplist[row])):
                if maplist[row][column] == 0:
                    self.canvas.create_image(column*72,row*72, image = self.floorimage, anchor= NW)
                else:
                    self.canvas.create_image(column*72,row*72, image = self.wallimage, anchor= NW)
        # self.root.mainloop()

    def create_hero_object(self, postionx, postiony):
        self.characters["hero"] = self.canvas.create_image(postionx*72, postiony*72, image = self.hero_images["down"], anchor= NW)

    # def move_hero_up(self, postionx, postiony):
    #     self.canvas.create_image(postionx*72, postiony*72, image = self.hero_images["up"], anchor= NW)

    def create_boss_object(self, postionx, postiony):
        self.characters["boss"] = self.canvas.create_image(postionx*72,postiony*72, image = self.bossimage, anchor = NW)

    # def create_skeletons_by_for(self, skeleton_list):
    #     for skeleton in skeleton_list:
    #         self.create_skeleton_object(skeleton)

    def create_skeleton_object(self, postionx, postiony):
        self.characters["skeletons"].append(self.canvas.create_image(postionx*72,postiony*72, image = self.skeleton, anchor = NW))

    def move(self, who, postionx, postiony, index=None):
        if type(index) == int:
            self.canvas.move(self.characters[who][index], postionx*72, postiony*72)
        else:
            self.canvas.move(self.characters[who], postionx*72, postiony*72)

    def mainloop_draw(self):
        self.root.mainloop()


# class Stat_Label:
#     pass

# mapom = GameMap()
