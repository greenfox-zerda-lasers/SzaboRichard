# Create a function that takes a string and creates a palindrome from it. It should work like this:

# output = create_palindrome('pear')

# print(output) # it prints: pearraep

def palind_funct(input):
     string = []
     for i in range(len(input)-1,-1, -1):
         string.append(input[i])
     return(string)

print(palind_funct("alma"))
