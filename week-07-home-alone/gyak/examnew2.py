# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def a_counter_from_file(file_name):
    try:
        f = open(file_name, "r")
        thefile = f.readlines()
        a_count = 0
        for lines in thefile:
            for char in lines:
                if char == "a":
                    a_count+= 1
        return a_count
    except FileNotFoundError:
        print(0)

print(a_counter_from_file("tree.txt"))
print(a_counter_from_file("testr.txt"))
