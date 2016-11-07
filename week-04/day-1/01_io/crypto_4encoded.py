# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    magic = ""
    for line in result:
        for string in line:
            if string != " " and string != "\n":
                magic += chr(ord(string)-1)
            else:
                magic += string

    f.close()
    return magic


print(decrypt('texts/encoded_zen_lines.txt'))
