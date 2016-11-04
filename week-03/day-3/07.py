# create a function that takes a list and returns a new list with all the elements doubled
def new_dobL(list):
    newl = []
    for i in list:
        newl += [2*i]
    return newl

my_list = [1, 2, 3]
print(new_dobL(my_list))
