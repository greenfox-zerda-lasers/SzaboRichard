# Union method

# Implement union method which combines two arrays.
def union(list_first, listcon):
    new = []
    for i in list_first:
        new += [i]
    for i in listcon:
        if i not in new:
            new.append(i)
    return(new)

print(union([4,5,6], [1,2,3]))
# expected output: [4,5,6,1,2,3]

print(union([4,5,7], [4,1,7]))
# expected output: [1,4,5,7]
