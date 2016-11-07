# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

# def triangle(line):
#     i = 0
#     x = 0
#     c = line+1
#     d = (' ')
#     while i <= line:
#      i+= 1
#      while x <= line:
#          x += 2
#          c -= 2
#          print(d * c + x * ('*')+("* ") + d*c +(' 12'))
#     print(('new line')* i)
#
# triangle(5)

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
