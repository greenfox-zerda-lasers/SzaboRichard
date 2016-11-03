# Sort

# Implement bubble sort method.
def bubble_sort(sort_it):
    for num in range(len(sort_it)-1,0,-1):
        for i in range(num):
            if sort_it[i] > sort_it[i+1]:
                temp = sort_it[i]
                sort_it[i] = sort_it[i+1]
                sort_it[i+1] = temp
    return sort_it

print(bubble_sort([3,9,4,5,2,1]))
# expected output: [1,2,3,4,5,9]
