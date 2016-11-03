numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)
def min_funt(num):
    mins = num[0]
    for i in num:
        if i < mins:
             mins = i
    return mins

print(min_funt(numbers))
