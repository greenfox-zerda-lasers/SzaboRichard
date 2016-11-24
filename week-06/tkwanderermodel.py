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
        # random.shuffle(self.tilemap)
        self.skeleton_list = []


    def add_more_skeleton(self):
        for _ in range(random.randint(3,7)):
            skeleton = Skeleton()
            self.skeleton_list.append(skeleton)
        return self.skeleton_list

class Character:
    def __init__(self):
        self.healthpoint = 0
        self.defencpoimt = 0
        self.strikepoint = 0
        self.d6roll = random.randint(1, 6)

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.postion = {"x" : 0, "y" : 0}

class Skeleton(Character):
    def __init__(self):
        self.map_data = Map_data()
        self.postion = {"x": 0, "y" : 0}
        self.skeletons_not_in_walls()
        self.monster_direction = ((0,1), (0,-1), (1,0), (-1,0))

    def skeletons_not_in_walls(self):
        postionx = random.randint(0,9)
        postiony = random.randint(0,9)
        if  self.map_data.tilemap[postiony][postionx] != 1:
            self.postion["x"] = postionx
            self.postion["y"] = postiony
        else:
            self.skeletons_not_in_walls()
