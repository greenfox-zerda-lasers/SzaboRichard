from tkinter import *
from PIL import Image, ImageTk

class GameMap:
    def __init__(self):
        self.tile = 72
        self.root = Tk()
        self.canvas = Canvas(self.root,width= 12*72, height= 11*72)
        self.im = ImageTk.PhotoImage(Image.open("C:/Users/ignoc/Desktop/Lightning/Demo day/sponsor demo/background.jpg"))
        self.canvas.pack()
        Canvas_Image = self.canvas.create_image(0,0, image=self.im, anchor="nw")
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

    def draw_label_hero(self, hero):
        label_frame = LabelFrame(self.canvas, text="Hero:")
        self.herohp = Label(label_frame, text="Healthpoint: "+ str(hero[0]))
        self.herodp = Label(label_frame, text="Defencepoint: "+ str(hero[1]))
        self.herosp = Label(label_frame, text="Strikepoint: "+ str(hero[2]))
        self.herohp.pack()
        self.herodp.pack()
        self.herosp.pack()
        self.canvas.create_window(720, 50, window=label_frame, anchor = W)

    def draw_label_enemies(self, data):
        label_frame = LabelFrame(self.canvas, text="Evil Enemy: ")
        self.enemyhp = Label(label_frame, text="Healthpoint: "+ str(data[0]))
        self.enemydp = Label(label_frame, text="Defencepoint: "+ str(data[1]))
        self.enemysp = Label(label_frame, text="Strikepoint: "+ str(data[2]))
        self.enemyhp.pack()
        self.enemydp.pack()
        self.enemysp.pack()
        self.canvas.create_window(720, 200, window=label_frame, anchor = W)



    def mainloop_draw(self):
        self.root.mainloop()
