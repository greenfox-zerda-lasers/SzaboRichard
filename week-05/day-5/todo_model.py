

class Todo_model:
    def __init__(self,filename):
        self.filename = filename

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
        f.close()
        f = open(self.filename, "w")
        for index, line in enumerate(lines):
            if index != int(inputt):
                f.write(line)
        f.close()
