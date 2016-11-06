# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

class ReverseTriangleDraw():
    lines = ""

    def draw_stars(self, lines):
        j = 1
        y = lines
        for i in range(lines):
            print(' ' * y + j * ('*'))
            j += 2
            y -= 1

# Total witchcraft, but it works's
        j = lines * 2 - 3
        y = 2
        for i in range(lines):
            print(' ' * y + j * ('*'))
            y += 1
            j -= 2

triangle = ReverseTriangleDraw()
triangle.draw_stars(10)
