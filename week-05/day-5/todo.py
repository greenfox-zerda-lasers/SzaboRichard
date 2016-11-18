import sys
from todo_view import TodoView
from todo_model import Todo_model

class TodoCtrl:
    def __init__(self):
        self.view = TodoView()
        self.model = Todo_model()
        self.input_list = sys.argv
        self.input_l_len = len(self.input_list)
        self.input_empty_print()

    def input_empty_print(self):
        print(self.input_list)
        if self.input_l_len == 1:
            print(self.view.usage_print['usage'])
        else:
            self.input_checker()

    def input_checker(self):
        if self.input_list[1] == '-l':
            self.if_shitty_file_is_empty_or_not()
        if self.input_list[2] == '-a':
            pass

    def if_shitty_file_is_empty_or_not(self):
        data = self.model.file_open_read("test.txt")
        if data == []:
            self.view.print_empty_shitty_file()
        else:
            self.view.print_this_shitty_file(data)



ctrl = TodoCtrl()
