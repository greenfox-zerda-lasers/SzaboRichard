# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    with open(file_name) as f:
        data = f.readlines()
        temp = ""
        for line in data:
            line.rstrip()
            for string in reversed(list(line)):
                temp += string
            temp += "\n"
        return temp
