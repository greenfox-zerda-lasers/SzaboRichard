# create a function that returns it's input factorial
def fact_function(numb):
    temp = 1
    for i in range(1,numb+1):
        temp *= i
    return temp

print(fact_function(5))
