# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def evry_second_item_from_alist(data_list):
    try:
        new_returned_list = []
        for i in data_list:
            if i % 2 == 0:
                new_returned_list.append(i)
        return new_returned_list
    except TypeError as param:
        print("{0}, is not a list".format(param))

example= [1, 2, 3, 4, 5]
print(evry_second_item_from_alist(example))
