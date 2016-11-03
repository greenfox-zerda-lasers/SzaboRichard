# Linear Search
# Implement linear search method.
# linear_search([4,5,6], 6)
# expected output: 2
# linear_search([4,5,7], 6)
# expected output: -1

def linear_search(search, num):
    pos = 0
    temp = -1
    for i in range(len(search)):
        temp += 1
        if search[i] == num:
            pos = temp
        else:
            pos = -1
    return pos

print(linear_search([4,5,6], 6))
# linear_search([4,5,7], 6)

print(linear_search([4,5,7], 6))
# expected output: -1
