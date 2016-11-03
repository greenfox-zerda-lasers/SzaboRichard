numbers = [3, 4, 5, 6, 7]
# # write a function that reverses a list
# def funt_reverse (number):
#     number.reverse()
#     print('List reverse:', number)
#
# funt_reverse(numbers)

def funt_reverse(number):
    new = []
    for i in range(len(number)-1,-1,-1):
        new.append(number[i])
    return new

print (funt_reverse(numbers))
