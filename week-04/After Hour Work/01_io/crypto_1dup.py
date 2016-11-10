# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    temp = ""
    for line in result:
        for index, string in enumerate(line):
            if index % 2 == 0:
              temp += string
    f.close()
    return temp
