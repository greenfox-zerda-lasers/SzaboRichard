from tkwandererview import GameMap
from tkwanderermodel import Map_data, Character, Hero, Skeleton, Boss
import random

class TkwandererMainControl:
    def __init__(self):
        self.viewGameMap = GameMap()
        self.map_data = Map_data()
        self.hero_data = Hero()
        self.skeleton_data = Skeleton()
        self.model_data_Game = Character()
        self.boss_data = Boss()
        self.skeleton_list = []

# ----------Draw map, hero, boss, skeleton(s)
        self.viewGameMap.draw_map(self.map_data.tilemap)
        self.add_more_skeleton()
        self.viewGameMap.create_hero_object(self.hero_data.postion["x"], self.hero_data.postion["y"])
        self.viewGameMap.create_boss_object(self.boss_data.postion["x"], self.boss_data.postion["y"])
        self.viewGameMap.create_skeletons_by_for(self.skeleton_list)

# ---------- 2 labels + indexer
        self.label_update_hero = (self.hero_data.healthpoint, self.hero_data.defencpoimt, self.hero_data.strikepoint)
        self.viewGameMap.draw_label_hero(self.label_update_hero)
        self.label_update = ("Empty" , "Empty", "Empty")
        self.viewGameMap.draw_label_enemies(self.label_update)
        self.movement_indexer = 0
        self.is_fight = False
# --------- char movement draw end
        self.character_step()
        self.viewGameMap.canvas.focus_set()
        self.viewGameMap.mainloop_draw()


    def add_more_skeleton(self):
        for _ in range(random.randint(3,7)):
            skeleton = Skeleton()
            self.skeleton_list.append(skeleton)

# ---------- MOVMENT METHODS HERO

    def character_step(self):
        self.viewGameMap.canvas.bind("<w>", self.movement_phases)
        self.viewGameMap.canvas.bind("<a>", self.movement_phases)
        self.viewGameMap.canvas.bind("<s>", self.movement_phases)
        self.viewGameMap.canvas.bind("<d>", self.movement_phases)
        self.viewGameMap.canvas.bind("<space>", self.fight_event)

    def movement_phases(self, event):
        self.enemy_stats_writer_skeleton_or_boss()
        self.movement_indexer+= 1
        self.move_enemies()
        if event.keysym == "w":
            self.move_up()
        if event.keysym == "s":
            self.move_down()
        if event.keysym == "d":
            self.move_right()
        if event.keysym == "a":
            self.move_left()

    def fight_event(self, event):
        if event.keysym == "space":
            self.fight()
            self.enemy_stats_writer_skeleton_or_boss()

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

# ------------ MOVEMENT METHODS ENEMIES

    def move_enemies(self):
        if self.movement_indexer % 2 == 0:
            x,y = random.choice(self.boss_data.boss_direction)
            if self.wall_checker(self.boss_data.postion["x"]+x, self.boss_data.postion["y"]+y):
                self.boss_data.postion["x"] += x
                self.boss_data.postion["y"] += y
                self.viewGameMap.move("boss", x, y)

            skelcount = 0
            for skeleton in self.skeleton_list:
                x,y = random.choice(skeleton.monster_direction)
                if self.wall_checker(skeleton.postion["x"]+x, skeleton.postion["y"]+y):
                    skeleton.postion["x"] += x
                    skeleton.postion["y"] += y
                    self.viewGameMap.move("skeletons", x, y, skelcount)
                skelcount += 1

# ----------- FIGHTING


    def fight(self):
        enemy = self.is_fighting()
        if enemy is not None:
            self.hero_data.strike(enemy)
            if enemy == self.boss_data:
                if self.boss_data.healthpoint <= 0:
                    print(enemy.healthpoint)
                    self.viewGameMap.canvas.delete(self.viewGameMap.characters["boss"])
            else:
                if enemy.healthpoint <= 0:
                    self.viewGameMap.canvas.delete(self.viewGameMap.characters["skeletons"][self.skeleton_list.index(enemy)])


    def is_fighting(self):
        for skeleton in self.skeleton_list:
            if skeleton.postion["x"] == self.hero_data.postion["x"] and skeleton.postion["y"] == self.hero_data.postion["y"]:
                if skeleton.alive is True:
                    return skeleton

        if self.boss_data.postion["x"] == self.hero_data.postion["x"] and self.boss_data.postion["y"] == self.hero_data.postion["y"]:
            if self.boss_data.alive is True:
                return self.boss_data
        return None

    def enemy_stats_writer_skeleton_or_boss(self):
        for skeleton in self.skeleton_list:
            if skeleton.postion["x"] == self.hero_data.postion["x"] and skeleton.postion["y"] == self.hero_data.postion["y"]:
                self.label_update = (skeleton.healthpoint, skeleton.defencpoimt, skeleton.strikepoint)
                self.viewGameMap.enemyhp.config(text="Healthpoint: "+str(self.label_update[0]))
                self.viewGameMap.enemydp.config(text="Defencepoint: "+str(self.label_update[1]))
                self.viewGameMap.enemysp.config(text="Strikepoint: "+str(self.label_update[2]))
                return self.label_update, self.label_update_hero

        if self.boss_data.postion["x"] == self.hero_data.postion["x"] and self.boss_data.postion["y"] == self.hero_data.postion["y"]:
            if self.boss_data.alive is True:
                self.label_update = (self.boss_data.healthpoint, self.boss_data.defencpoimt, self.boss_data.strikepoint)
                self.viewGameMap.enemyhp.config(text="Healthpoint: "+str(self.label_update[0]))
                self.viewGameMap.enemydp.config(text="Defencepoint: "+str(self.label_update[1]))
                self.viewGameMap.enemysp.config(text="Strikepoint: "+str(self.label_update[2]))
                return self.label_update, self.label_update_hero

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
