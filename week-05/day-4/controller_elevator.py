from model_elevator import Elevator_model
from view_elevator import Elevator_view
# import time
# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

class ElevatorCTRL:
    def __init__(self):
        self.model = Elevator_model()
        self.view = Elevator_view()
        self.elev_start()

    def elev_start(self):
        # self.clear_console()
        self.view.print_welcome_msg()
        self.view.print_add_people()
        self.num_valid_rec_add_people_check()
        self.game_loop()


    def game_loop(self):
        self.view.print_game_loop()
        self.num_valid_rec_floor_check()
        self.view.draw_building(self.model.floors, self.model.floor_stands, self.model.elevator_people)
        print("Do you want to remove some lads?")
        self.model.remove_people(self.num_input_check())
        print("Up for more play?(y) (n)")
        self.game_restart()

    def num_input_check(self):
        try:
            userinput = int(input())
            return userinput
        except ValueError:
            print("Please feed me with numbers")
            return self.num_input_check()

    def num_valid_rec_add_people_check(self):
        is_valid_number = False
        while not is_valid_number:
            userinput = self.num_input_check()
            if userinput >= 0 and userinput <= 12:
                self.model.add_people(userinput)
                is_valid_number = True
            else:
                print("Please give me a num less than 12!")

    def num_valid_rec_floor_check(self):
        is_valid_number = False
        while not is_valid_number:
            userinput = self.num_input_check()
            if userinput >= 0 and userinput <= 10:
                self.model.floor_now(userinput)
                is_valid_number = True
            else:
                print("Please give me a num less than 10!")

    def game_restart(self):
        runningTrue = True
        while runningTrue:
            inputt = input()
            if inputt == "y":
                self.elev_start()
                runningTrue = False
            elif inputt == "n":
                print("Thx for the game cya")
                runningTrue = False
            else:
                print("Give me valid answer, y or n")




ctrl = ElevatorCTRL()
