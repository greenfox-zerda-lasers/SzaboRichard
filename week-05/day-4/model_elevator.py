
# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling
class Elevator_model:
    def __init__(self):
        # self.ctrl = ElevatorCTRL()
        self.elevator_people = 0
        self.floors = 12
        self.floor_stands = 0

    def floor_now(self, inputt):
        self.floor_stands = inputt

    def floor_move_up(self):
        self.floor_stands += 1

    def floor_move_down(self):
        self.floor_stands -= 1

    def people_in_the_elevator(self):
        return self.elevator_people

    def add_people(self, inputt):
        self.elevator_people += inputt
        return self.elevator_people


    def remove_people(self, inputt):
        self.elevator_people -= inputt
        return self.elevator_people


# elev = controller_elevator.ElevatorCTRL()
model = Elevator_model()
