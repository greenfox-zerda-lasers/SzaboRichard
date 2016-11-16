# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).
def bunnies_yay(n):
    if n == 1:
        return 2
    else:
        return 2 + bunnies_yay(n-1)

print(bunnies_yay(10))
