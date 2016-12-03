# garden app JAVA exam

class Garden:
    def __init__(self):
        self.garden_plant_holder = []

    def add_flowers(self,flower_number, flower_name):
        for _ in range(flower_number):
            flower = Flower(flower_name)
            self.garden_plant_holder.append(flower)

    def add_trees(self, tree_number, tree_name):
        for _ in range(tree_number):
            tree = Tree(tree_name)
            self.garden_plant_holder.append(tree)

    def garden_printer(self):
        for plant in self.garden_plant_holder:
            if isinstance(plant, Flower):
                if plant.is_thirsty:
                    print("The {0} Flower needs water".format(plant.flower_name))
                else:
                    print("The {0} Flower does not need water".format(plant.flower_name))

            elif isinstance(plant, Tree):
                if plant.is_thirsty:
                    print("The {0} Tree needs water".format(plant.tree_name))
                else:
                    print("The {0} Tree does not need water".format(plant.tree_name))

    def watering_the_plants(self, water_amount):
        water_divide = len(self.garden_plant_holder)
        print("Watering with: ", water_amount)
        for plant in self.garden_plant_holder:
            if isinstance(plant, Flower):
                if plant.is_thirsty:
                    plant.watering_the_flower(water_amount/water_divide)
                    water_divide -= 1
                    print(water_divide)
                    if plant.is_thirsty == False:
                        print("The {0} Flower does not need water".format(plant.flower_name))
                    else:
                        print("The {0} Flower needs water".format(plant.flower_name))
                else:
                    print(water_divide)
                    water_divide -= 1
                    print("The {0} Flower does not need water".format(plant.flower_name))
            elif isinstance(plant, Tree):
                if plant.is_thirsty:
                    plant.watering_the_tree(water_amount/water_divide)
                    # print(water_amount/water_divide)
                    water_divide -= 1
                    print(water_divide)
                    if plant.is_thirsty == False:
                        print("The {0} Tree does not need water".format(plant.tree_name))
                    else:
                        print("The {0} Tree needs water".format(plant.tree_name))
                else:
                    print("The {0} Tree does not need water".format(plant.tree_name))

class Flower:
    def __init__(self, flower_name):
        self.flower_name = flower_name
        self.water_lvl = 0
        self.is_thirsty = True

    def watering_the_flower(self, water):
        absorbed_water = water *0.75
        if absorbed_water > 5:
            self.is_thirsty = False
        self.water_lvl += absorbed_water

class Tree:
    def __init__(self, tree_name):
        self.tree_name = tree_name
        self.water_lvl = 0
        self.is_thirsty = True

    def watering_the_tree(self, water):
        absorbed_water = water*0.40
        if absorbed_water > 10:
            self.is_thirsty = False
        self.water_lvl += absorbed_water

my_garden = Garden()
my_garden.add_flowers(1, "yellow")
my_garden.add_flowers(1, "blue")
my_garden.add_trees(1, "purple")
my_garden.add_trees(1, "orange")
my_garden.garden_printer()
my_garden.watering_the_plants(40)
my_garden.watering_the_plants(70)
