# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def every_second_item_to_new_list(list_param):
    try:
        second_items_list = []
        for i in range(len(list_param)):
            if i % 2 == 1:
                second_items_list.append(list_param[i])
        return second_items_list
    except TypeError:
        print("Please give me a list for input!")

# example = 1
example = [1, 2, 3, 4, 5]
print(every_second_item_to_new_list(example))
