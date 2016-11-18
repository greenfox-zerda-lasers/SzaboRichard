

class TodoView:
    def __init__(self):
        self.usage_print = {
            "usage" : """
            Python Todo application
            =======================

            Command line arguments:
            -l   Lists all the tasks
            -a   Adds a new task
            -r   Removes an task
            -c   Completes an task""",
        }

    def print_this_shitty_file(self, data):
        for i, value in enumerate(data,start=1):
            print(str(i), value.rstrip())

    def print_empty_shitty_file(self):
        print("No todos for today! :)")
