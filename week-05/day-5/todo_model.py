# import os.path
# from pathlib import path

class Todo_model:
    def __init__(self,filename):
        self.filename = filename
        try:
            open(self.filename)
        except FileNotFoundError:
            self.new_file_write()

    def new_file_write(self):
        f = open(self.filename, "w")
        f.close()

    def file_open_read(self):
        f = open(self.filename)
        data = f.readlines()
        f.close()
        return data

    def file_write(self, inputt):
        f = open(self.filename, "a")
        data = f.write("\n"+inputt)
        f.close()
        return data

    def file_delete_by_lines(self, inputt):
        # print("fut-e", inputt)3
        f = open(self.filename, "r")
        lines = f.readlines()
        # print(len(lines), int(inputt))
        if len(lines) >= int(inputt):
            f.close()
            f = open(self.filename, "w")
            for index, line in enumerate(lines,start=1):
                if index != int(inputt):
                    f.write(line)
            f.close()
        else:
            raise IndexError

    # def if_shitty_file_exits(self,filename):
    #     if filename.is_file():
    #         pass
    #     else:
    #         self.new_file_write()
