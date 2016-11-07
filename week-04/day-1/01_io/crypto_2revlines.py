# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    eredm = ""
    index=[]
    for line in result:
        line = line.rstrip()
        for string in reversed(list(line)):
            eredm += string
        eredm += "\n"
    f.close()
    return eredm



    # with open(file_name, 'r') as f:
    #     for line in reversed(list(f.readlines())):
    #         return(line)
