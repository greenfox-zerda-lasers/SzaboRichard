import sys
from todo_view import TodoView

class TodoCtrl:
    def __init__(self):
        self.view = TodoView()

    def sys_args_checker(self):
        print(sys.argv)
        if len(sys.argv) == 1:
            print("No argument was given")
        elif len(sys.argv) > 1:
            print(self.view.usage_print['usage'])
