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
        self.healthpoint = 0
        self.defencpoimt = 0
        self.strikepoint = 0
        self.d6roll = random.randint(1, 6)
        self.alive = True

    def strike(self, defender):
        self.d6roll = random.randint(1, 6)
        if (self.strikepoint + 2*self.d6roll) > defender.defencpoimt:
            defender.healthpoint -= (self.strikepoint-defender.defencpoimt)
            defender.is_alive()
        else:
            self.healthpoint -= (defender.strikepoint-self.healthpoint)
            self.is_alive()

    def is_alive(self):
        if self.healthpoint > 0:
            self.alive = True
        elif self.healthpoint <= 0:
            self.alive = False
# on a strike a strike value (SV) is calculated from SP and a d6 doubled
# the strike is successful if 2*d6 + SP is higher than the other character's DP
# on a successful strike the other character's HP is decreased by the SV - the other character's DP

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.d6roll = random.randint(1, 6)
        self.healthpoint = 20 + 3 * self.d6roll
        self.defencpoimt = 2 * self.d6roll
        self.strikepoint = 5 + self.d6roll
        self.postion = {"x" : 0, "y" : 0}

class Skeleton(Character):
    def __init__(self):
        super().__init__()
        self.d6roll = random.randint(1, 6)
        self.healthpoint = 2 * self.d6roll
        self.defencpoimt = 2 * self.d6roll
        self.strikepoint = self.d6roll
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

    # x y hasonlítgatás iterálás skel_listen, +boss should fight
    # should fight = false amikor végig a skeletonoon amikor megegy az x és az y akkor true ha nem akkor false


class Boss(Character):
    def __init__(self):
        super().__init__()
        self.d6roll = random.randint(1, 6)
        self.postion = {"x": 7, "y" : 6}
        self.boss_direction = ((0,1), (0,-1), (1,0), (-1,0))
        self.healthpoint = 2 * self.d6roll + self.d6roll
        self.defencpoimt = 2 * self.d6roll + self.d6roll / 2
        self.strikepoint = self.d6roll
