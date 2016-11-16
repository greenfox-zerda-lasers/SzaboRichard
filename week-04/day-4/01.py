# 1. write a recursive function
# that takes one parameter: n
# and counts down from n
def first_rec_funct(n):
    if n <= 1:
        print(n)
    else:
        print(n)
        first_rec_funct(n-1)

first_rec_funct(5)
