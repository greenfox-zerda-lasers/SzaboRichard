names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
def funct_short_str(name_l):
    min_name = name_l[0]
    for i in name_l:
        if len(i) < len(min_name):
            min_name = i
    return min_name
print (funct_short_str(names))
