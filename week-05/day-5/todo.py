import sys
from todo_view import TodoView
from todo_model import Todo_model

class TodoCtrl:
    def __init__(self):
        self.view = TodoView()
        self.model = Todo_model("test.txt")
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
        elif self.input_list[1] == '-a' and self.input_l_len == 2:
            self.view.add_task_error_handling_print()
        elif self.input_list[1] == '-a' and self.input_l_len > 2:
            self.model.file_write(self.input_list[2])
            self.if_shitty_file_is_empty_or_not()
        elif self.input_list[1] == '-r' and self.input_l_len == 2:
            self.view.remove_task_error_handling_print()
        elif self.input_list[1] == '-r' and self.input_l_len > 2:
            try:
                self.model.file_delete_by_lines(self.input_list[2])
            except IndexError:
                print("Unable to remove: Index is out of bound")
            except ValueError:
                print("Unable to remove: Index is not a number")
        # if self.input_list[1] == 'c':
        #     pass
        else:
            print(self.view.usage_print['usage'])
            print("Unsupported argument")

    def if_shitty_file_is_empty_or_not(self):
        data = self.model.file_open_read()
        if data == []:
            self.view.print_empty_shitty_file()
        else:
            self.view.print_this_shitty_file(data)





ctrl = TodoCtrl()
