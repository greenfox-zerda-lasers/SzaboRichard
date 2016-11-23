import random

class Map_data:
    def __init__(self):
        self.tilemap = [
        [0,0,0,1,0,1,0,0,0,0],
        [0,0,0,1,0,1,0,1,1,0],
        [0,1,1,1,0,1,0,1,1,0],
        [0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,0,1,1,1,1,0],
        [0,1,0,1,0,0,0,0,1,0],
        [0,1,0,1,0,1,1,0,1,0],
        [0,0,0,0,0,1,1,0,1,0],
        [0,1,1,1,0,0,0,0,1,0],
        [0,0,0,1,0,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,0,0]
        ]

class Character:
    def __init__(self):
        self.skeleton_list = []
        # self.skeleton = Skeleton()

    def add_more_skeleton(self, skeleton_num):
        for i in range(skeleton_num):
            skeleton = Skeleton()
            self.skeleton_list.append(skeleton)

class Hero(Character):
    def __init__(self):
        self.postion = {"x" : 0, "y" : 0}

class Skeleton:
    def __init__(self):
        self.postion = {"x": 0, "y" : 0}
        self.monster_direction = ((0,1), (0,-1), (1,0), (-1,0))
