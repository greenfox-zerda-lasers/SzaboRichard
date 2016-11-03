numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function
def my_sum_funct (args):
    total = 0
    for a in args:
        total += a
        print (total)

print(my_sum_funct(numbers))
# my_sum_funct(len(numbers), numbers[0])
# my_sum_funct(numbers[1], numbers[3])
