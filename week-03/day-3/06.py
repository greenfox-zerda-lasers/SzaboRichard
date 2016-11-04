# create a function that takes a list and returns a new list that is reversed
def list_taking(list):
    newl = []
    for i in range(len(list)-1, -1, -1):
        newl += [list[i]]
    return newl

my_list = [1, 2, 3]
print(list_taking(my_list))
