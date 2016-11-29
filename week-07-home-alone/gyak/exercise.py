

class Garden:
    def __init__(self):
        self.my_little_garden = []
        self.thirsty_plants = 0
        self.water_each = 0

    def plant_flower(self, amount, flower_type):
        for _ in range(amount):
            flower = Flower(flower_type)
            self.my_little_garden.append(flower)

    def plant_tree(self, amount, tree_type):
        for _ in range(amount):
            tree = Tree(tree_type)
            self.my_little_garden.append(tree)

    def garden_printer(self):
        for plant in self.my_little_garden:
            if isinstance(plant, Flower):
                if plant.flower_needs_water == True:
                    print("The {0} flower needs water".format(plant.flower_type))
                else:
                    print("The {0} flower does not need water".format(plant.flower_type))

            elif isinstance(plant, Tree):
                if plant.tree_needs_water == True:
                    print("The {0} flower needs water".format(plant.tree_type))
                else:
                    print("The {0} flower does not need water".format(plant.tree_type))

    def how_many_thirsty_plants_do_we_have(self):
        for plant in self.my_little_garden:
            if isinstance(plant, Flower):
                if plant.flower_needs_water == True:
                    if self.thirsty_plants < len(self.my_little_garden):
                        self.thirsty_plants += 1
                else:
                    self.thirsty_plants -= 1

            elif isinstance(plant, Tree):
                if plant.tree_needs_water == True:
                    if self.thirsty_plants < len(self.my_little_garden):
                        self.thirsty_plants +=1
                else:
                    self.thirsty_plants -= 1


    def water_the_plants(self, amount):
        self.how_many_thirsty_plants_do_we_have()
        # print(self.thirsty_plants)
        print("Watering with ", amount)
        for plant in self.my_little_garden:
            if isinstance(plant, Flower):
                if plant.flower_needs_water == True:
                    # print(self.thirsty_plants, " oszto")
                    self.water_each = amount / self.thirsty_plants
                    # print(self.thirsty_plants, " oszto")
                    plant.water_the_flower(self.water_each)
                    # print(plant.flower_needs_water)
                    self.how_many_thirsty_plants_do_we_have()
                    if self.water_each > 5:
                        print("The {0} flower does not need water".format(plant.flower_type))
                    else:
                        print("The {0} flower needs water".format(plant.flower_type))
                    print(self.thirsty_plants, " oszto")
                else:
                    print("The {0} flower does not need water".format(plant.flower_type))

            if isinstance(plant, Tree):
                self.how_many_thirsty_plants_do_we_have()
                print(self.water_each)
                if plant.tree_needs_water == True:
                    self.how_many_thirsty_plants_do_we_have()
                    plant.water_the_tree(self.water_each)
                # print(water_each)
                    if self.water_each > 10:
                        print("The {0} tree does not need water".format(plant.tree_type))
                    else:
                        print("The {0} tree needs water".format(plant.tree_type))
                else:
                    print("The {0} tree needs water".format(plant.tree_type))


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
