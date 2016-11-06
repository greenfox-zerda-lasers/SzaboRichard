# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def print_star(param):
    x = 0
    while x <= param:
        x += 1
        print (x * ('*'))

print_star(4)
