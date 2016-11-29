

class Garden:
    def __init__(self):
        self.my_little_garden_flower = []
        self.my_little_garden_tree = []

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


    def water_the_plants(self, amount):
        water_each = amount/4
        print("Watering with ", amount)
        for plant in self.my_little_garden_flower:
            if plant.flower_needs_water == True:
                plant.water_the_flower(water_each)
                if water_each*0.7 > 5:
                    print("The {0} flower does not need water".format(plant.flower_type))
                else:
                    print("The {0} flower needs water".format(plant.flower_type))
            else:
                print("The {0} flower does not need water".format(plant.flower_type))

        for tree in self.my_little_garden_tree:
            if tree.tree_needs_water == True:
                tree.water_the_tree(water_each)
                if water_each*0.4 > 10:
                    print("The {0} tree does not need water".format(tree.tree_type))
                else:
                    print("The {0} tree needs water".format(tree.tree_type))
            else:
                print("The {0} tree does not need water".format(tree.tree_type))



class Flower:
    def __init__(self, flower_type):
        self.water_level = 0
        self.flower_needs_water = True
        self.flower_type = flower_type

    def water_the_flower(self, water_amount):
        if self.water_level < 5:
            self.water_level = water_amount*0.75
        else:
            self.flower_needs_water = False

class Tree:
    def __init__(self, tree_type):
        self.water_level = 0
        self.tree_needs_water = True
        self.tree_type = tree_type

    def water_the_tree(self, water_amount):
        if self.water_level < 10:
            self.water_level = water_amount*0.4
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
# print(my_first_garden.my_little_garden)
