# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    eredm = ""
    for line in result:
        for i, c in enumerate(line):
            if i % 2 == 0:
                eredm += c
    f.close()
    return eredm
