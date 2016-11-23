from tkwandererview import GameMap
from tkwanderermodel import Character, Map_data, Hero, Skeleton
import random

class TkwandererMainControl:
    def __init__(self):
        self.viewGameMap = GameMap()
        self.map_data = Map_data()
        self.hero_data = Hero()
        self.skeleton_data = Skeleton()
        self.model_data_Game = Character()
        self.viewGameMap.draw_map(self.map_data.tilemap)
        self.viewGameMap.create_hero_object(self.hero_data.postion["x"], self.hero_data.postion["y"])
        self.viewGameMap.create_boss_object(7,5)
        # self.viewGameMap.create_skeleton_object(2,6)
        self.viewGameMap.create_skeleton_object(self.skeleton_data.postion["x"],0)
        self.movement_indexer = 0
        self.character_step()
        self.viewGameMap.canvas.focus_set()
        self.viewGameMap.mainloop_draw()

        # wasd validator method, még egy függvény amibe bele a wasdos methodok

    # def add_and_draw_skeleton(self):
    #     self.model_data_Game.add_more_skeleton(3)
    #     self.viewGameMap.


    def character_step(self):
        self.viewGameMap.canvas.bind("<w>", self.growth)
        self.viewGameMap.canvas.bind("<a>", self.growth)
        self.viewGameMap.canvas.bind("<s>", self.growth)
        self.viewGameMap.canvas.bind("<d>", self.growth)

    def growth(self, event):
        self.movement_indexer+= 1
        self.move_enemies()
        print(self.hero_data.postion["x"],self.hero_data.postion["y"])
        # print(event.keysym)
        if event.keysym == "w":
            self.move_up()
        if event.keysym == "s":
            self.move_down()
        if event.keysym == "d":
            self.move_right()
        if event.keysym == "a":
            self.move_left()
        # print(self.movement_indexer)

    def move_down(self):
        if self.wall_checker(self.hero_data.postion["x"], self.hero_data.postion["y"]+1):
            self.hero_data.postion["y"]+=1
            self.viewGameMap.move("hero", 0, 1)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["down"])

    def move_up(self):
        if self.wall_checker(self.hero_data.postion["x"], self.hero_data.postion["y"]-1):
            self.hero_data.postion["y"] -= 1
            self.viewGameMap.move("hero",0,-1)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["up"])

    def move_right(self):
        if self.wall_checker(self.hero_data.postion["x"]+1, self.hero_data.postion["y"]):
            self.hero_data.postion["x"] += 1
            self.viewGameMap.move("hero",1,0)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["right"])


    def move_left(self):
        if self.wall_checker(self.hero_data.postion["x"]-1, self.hero_data.postion["y"]):
            self.hero_data.postion["x"] -= 1
            self.viewGameMap.move("hero",-1,0)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["left"])

    def move_enemies(self):
        if self.movement_indexer % 2 == 0:
            x,y = random.choice(self.skeleton_data.monster_direction)
            print(x,y)
            print(self.skeleton_data.postion["x"]+x, self.skeleton_data.postion["y"]+y)
            print(self.wall_checker(self.skeleton_data.postion["x"]+x, self.skeleton_data.postion["y"]+y))
            if self.wall_checker(self.skeleton_data.postion["x"]+x, self.skeleton_data.postion["y"]+y):
                self.skeleton_data.postion["x"] += x
                self.skeleton_data.postion["y"] += y
                self.viewGameMap.move("skeletons", x, y, 0)


    def wall_checker(self, postionx, postiony):
        if len(self.map_data.tilemap)-1 < postiony or  postiony < 0:
            return False
        elif len(self.map_data.tilemap)-2 < postionx or postionx < 0:
            return False
        elif (self.map_data.tilemap[postiony][postionx] == 1 ):
            return False
        else:
            return True


game = TkwandererMainControl()
