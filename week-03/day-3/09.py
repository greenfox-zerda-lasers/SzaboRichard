# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def print_star(param):
    star ="*"
    x = 0
    while x <= param:
        print(star)
        x += 1
        for i in range(x):
            print(star)

print_star(3)
