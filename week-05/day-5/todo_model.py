

class Todo_model:
    def __init__(self):
        pass

    def file_open_read(self, inputt):
        f = open(inputt)
        data = f.readlines()
        return data
    
