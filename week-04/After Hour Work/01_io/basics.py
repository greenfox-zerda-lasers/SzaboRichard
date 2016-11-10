# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

#print(readfile('texts/zen_of_python.txt'))

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    result = f.readlines()[number-1].rstrip()
    return result

print(readline('texts/zen_of_python.txt', 2))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    temp = ""
    for i in sentence:
        if  i != ".":
          temp += i
    return temp.split()

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    return " ".join(words) + '.'


# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    temp = []
    for i in string:
        temp += [ord(i)]
    return temp

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
        temp = ""
        for i in char_codes:
            temp += chr(i)
        print(temp)
        return temp
