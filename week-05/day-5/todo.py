import sys
from todo_view import TodoView

class TodoCtrl:
    def __init__(self):
        self.view = TodoView()
        self.input_list = ["todo.py"]
        self.input_l_len = len(self.input_list)
        self.sys_args_checker()

    def sys_args_checker(self):
        print(self.input_list)
        if self.input_l_len == 1:
            print(self.view.usage_print['usage'])


    def file_open_read(self, inputt):
        f = open(inputt)
        data = f.readlines()

ctrl = TodoCtrl()
