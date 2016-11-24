from tkinter import *
from PIL import Image, ImageTk

class GameMap:
    def __init__(self):
        self.tile = 72
        self.root = Tk()
        self.canvas = Canvas(self.root,width= 11.5*72, height= 11*72)
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


    def create_boss_object(self, postionx, postiony):
        self.characters["boss"] = self.canvas.create_image(postionx*72,postiony*72, image = self.bossimage, anchor = NW)

    def create_skeletons_by_for(self, skeleton_list):
        for skeleton in skeleton_list:
            self.create_skeleton_object(skeleton)

    def create_skeleton_object(self, skeleton):
        self.characters["skeletons"].append(self.canvas.create_image(skeleton.postion["x"]*72, skeleton.postion["y"]*72, image = self.skeleton, anchor = NW))

    def move(self, who, postionx, postiony, index=None):
        if type(index) == int:
            self.canvas.move(self.characters[who][index], postionx*72, postiony*72)
        else:
            self.canvas.move(self.characters[who], postionx*72, postiony*72)

    def draw_label_hero(self, hp, dp, sp):
        label_frame = LabelFrame(self.canvas, text="Hero:")
        label = Label(label_frame, text="Healthpoint: "+ str(hp))
        label2 = Label(label_frame, text="Defencepoint: "+ str(dp))
        label3 = Label(label_frame, text="Strikepoint: "+ str(sp))
        label.pack()
        label2.pack()
        label3.pack()
        self.canvas.create_window(720, 400, window=label_frame, anchor = W)

    def draw_label_enemies(self, healthpoint = 0, defencpoimt = 0, strikepoint = 0):
        label_frame = LabelFrame(self.canvas, text="Evil Enemy: ")
        label = Label(label_frame, text="Healthpoint: "+ str(healthpoint))
        label2 = Label(label_frame, text="Defencepoint: "+ str(defencpoimt))
        label3 = Label(label_frame, text="Strikepoint: "+ str(strikepoint))
        label.pack()
        label2.pack()
        label3.pack()
        self.canvas.create_window(720, 600, window=label_frame, anchor = W)



    def mainloop_draw(self):
        self.root.mainloop()
