

class Garden:
    def __init__(self):
        self.my_little_garden_flower = []
        self.my_little_garden_tree = []
        self.thirsty_plants = 0

    def plant_flower(self, amount, flower_type):
        for _ in range(amount):
            flower = Flower(flower_type)
            self.my_little_garden_flower.append(flower)

    def plant_tree(self, amount, tree_type):
        for _ in range(amount):
            tree = Tree(tree_type)
            self.my_little_garden_tree.append(tree)

    def garden_printer(self):
        for plant in self.my_little_garden_flower:
            if plant.flower_needs_water == True:
                print("The {0} flower needs water".format(plant.flower_type))
            else:
                print("The {0} flower does not need water".format(plant.flower_type))

        for tree in self.my_little_garden_tree:
            if tree.tree_needs_water == True:
                print("The {0} flower needs water".format(tree.tree_type))
            else:
                print("The {0} flower does not need water".format(tree.tree_type))

    def how_many_thirsty_plants_do_we_have(self):
        for flower in self.my_little_garden_flower:
            if flower.flower_needs_water == True:
                if self.thirsty_plants <= len(self.my_little_garden_tree):
                    self.thirsty_plants += 1
                else:
                    self.thirsty_plants -= 1

        for tree in self.my_little_garden_tree:
            if tree.tree_needs_water == True:
                if self.thirsty_plants <= len(self.my_little_garden_tree):
                    self.thirsty_plants +=1
                else:
                    self.thirsty_plants -= 1


    def water_the_plants(self, amount):
        self.how_many_thirsty_plants_do_we_have()
        water_each = amount / self.thirsty_plants
        print("Watering with ", amount)
        print(self.thirsty_plants)
        for plant in self.my_little_garden_flower:
            if plant.flower_needs_water == True:
                if water_each*0.75 > 5:
                    print("The {0} flower does not need water".format(plant.flower_type))
                else:
                    print("The {0} flower needs water".format(plant.flower_type))
                plant.water_the_flower(water_each)
            else:
                print("The {0} flower does not need water".format(plant.flower_type))

        for tree in self.my_little_garden_tree:
            if tree.tree_needs_water == True:
                # print(water_each)
                if water_each* 0.4 > 10:
                    print("The {0} tree does not need water".format(tree.tree_type))
                else:
                    print("The {0} tree needs water".format(tree.tree_type))
                tree.water_the_tree(water_each)
            else:
                print("The {0} tree needs water".format(tree.tree_type))



class Flower:
    def __init__(self, flower_type):
        self.water_level = 0
        self.flower_needs_water = True
        self.flower_type = flower_type

    def water_the_flower(self, water_amount):
        if self.water_level < 5:
            self.water_level += water_amount*0.75
        else:
            self.flower_needs_water = False

class Tree:
    def __init__(self, tree_type):
        self.water_level = 0
        self.tree_needs_water = True
        self.tree_type = tree_type

    def water_the_tree(self, water_amount):
        if self.water_level < 10:
            self.water_level += water_amount*0.40
        else:
            self.tree_needs_water = False

my_first_garden = Garden()
my_first_garden.plant_flower(1, "yellow")
my_first_garden.plant_flower(1, "blue")
my_first_garden.plant_tree(1, "purple")
my_first_garden.plant_tree(1, "orange")
my_first_garden.garden_printer()
my_first_garden.water_the_plants(40)
my_first_garden.water_the_plants(70)
# print(my_first_garden.my_little_garden_tree, my_first_garden.my_little_garden_flower)
