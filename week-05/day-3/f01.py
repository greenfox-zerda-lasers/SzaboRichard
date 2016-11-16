# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def num_divide(num):
    try:
        return 10 / num
    except ZeroDivisionError:
        return("fail")
    except TypeError:
        return("please give me a number")
