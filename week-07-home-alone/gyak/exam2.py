# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def file_writer_three_times_in_one_run(file_name, user_input):
    try:
        f = open(file_name, "w")
        f.write(user_input)
        f.write(user_input)
        f.write(user_input)
    except EnvironmentError as param:
        print(param)

file_writer_three_times_in_one_run("tree.txt", "apple")
