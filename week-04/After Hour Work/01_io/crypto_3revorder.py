# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    temp = []
    for i in range(len(result)-1,-1,-1):
        temp.append(result[i])
    f.close()
    return "".joint(temp)
