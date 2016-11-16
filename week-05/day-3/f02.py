# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_reader(filename):

    try:
        f = open(filename)
        readlines = f.readlines()
        linestemp = 0
        for lines in readlines:
            linestemp += 1
        return linestemp
    except IOError:
        return("0")



# print(file_reader("text.txt"))
