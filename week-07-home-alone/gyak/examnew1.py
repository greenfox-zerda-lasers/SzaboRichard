# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def element_doubler_in_list(data_list):
    try:
        doubled_element_list = []
        for element in data_list:
            doubled_element_list.append(element*2)
        return doubled_element_list
    except TypeError as error_param:
        print("{0}, is not a list".format(error_param))

checklist = [1,2,3,4]
fail = 1
print(element_doubler_in_list(checklist))
print(element_doubler_in_list(fail))
