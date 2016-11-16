# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n
def funct_rec_numAdd(n):
    if n <= 1:
        return n
    else:
        return n + funct_rec_numAdd(n-1)

print(funct_rec_numAdd(4))
