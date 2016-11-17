import time
import os
# Create a class the displays the Elevator art and navigation (list of commands)

class Elevator_view:
    def __init__(self):
        self.building = {
            "floor0" :  " .'_______________________________`.",
            "floor" :   "    || ||       || ||       || || ",
            "floorXe" : "   _||_||_[___]_||_||_______||_||_ ",
            "floorX" :  "   _||_||_[_X_]_||_||_______||_||_",
            "floortop" :"  ___________________________________\n `._______________________________.'"
        }

        self.texts = {
            "welcomemsg" : "Welcome dear user. This is a godforsaken elevator game, and you can play with it.\n The elevator is empty right now, and it stands in the 0th florr.",
            "addp" : "Do you want to add some people to the elevator?",
            "floorn" : "Now give me a floor number!",
            }

    def print_welcome_msg(self):
        print(self.texts['welcomemsg'])

    def print_add_people(self):
        print(self.texts['addp'])

    def print_game_loop(self):
        print(self.texts['floorn'])

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')


    def draw_building(self, floor, floorstand, fpeople):
        self.cls()
        print(self.building['floortop'])
        # time.sleep()
        for i in range(floor,-1,-1):
            # time.sleep(1)
            if i == floorstand:
                if fpeople > 0:
                    print(self.building['floorX'])
                else:
                    print(self.building['floorXe'])
            else:
                print(self.building['floor'])
        print(self.building['floor0'])
        # ciklus ide draw
# lift = Elevator_view()
# lift.draw_building(10,0,1)
