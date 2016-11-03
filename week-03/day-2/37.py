numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def funt_filter(num):
    new = []
    for i in num:
        if i % 2 == 0:
            print("")
        else:
            new.append(i)
    return new

print(funt_filter(numbers))
