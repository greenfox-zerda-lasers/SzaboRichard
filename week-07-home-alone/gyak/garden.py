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

    # def garden_printer(self):

    def watering_the_plants(self, water_amount):

        thirsty_plants_count = 0
        for plant in self.garden_plant_holder:
            if plant.get_is_thirsty():
                thirsty_plants_count += 1

        if water_amount>0:
            print("Watering with: ", water_amount)

        for plant in self.garden_plant_holder:
            if plant.get_is_thirsty():
                plant.watering(water_amount/thirsty_plants_count)

            if plant.get_is_thirsty():
                print("The {0} {1} need water ({2})".format(plant.name, plant.__class__.__name__, plant.water_lvl))
            else:
                print("The {0} {1} does not need water ({2})".format(plant.name, plant.__class__.__name__, plant.water_lvl))
class Flower:
    def __init__(self, name):
        self.name = name
        self.water_lvl = 0
        self.is_thirsty = True

    def watering(self, water):
        self.water_lvl += water *0.75
        self.is_thirsty = self.get_is_thirsty()

    def get_is_thirsty(self):
        return (self.water_lvl < 5)

class Tree:
    def __init__(self, name):
        self.name = name
        self.water_lvl = 0
        self.is_thirsty = True

    def watering(self, water):
        self.water_lvl += water*0.40
        self.is_thirsty = self.get_is_thirsty()

    def get_is_thirsty(self):
        return (self.water_lvl < 10)

my_garden = Garden()
my_garden.add_flowers(1, "yellow")
my_garden.add_flowers(1, "blue")
my_garden.add_trees(1, "purple")
my_garden.add_trees(1, "orange")
# my_garden.garden_printer()
my_garden.watering_the_plants(0)
my_garden.watering_the_plants(40)
my_garden.watering_the_plants(70)
