# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has


class TriangleDraw():
    line = ""

    def draw_stars(self, lines):
        j = 1
        y = lines
        for i in range(lines):
            print(' ' * y + j * ('*'))
            j += 2
            y -= 1

triangle = TriangleDraw()
triangle.draw_stars(10)
