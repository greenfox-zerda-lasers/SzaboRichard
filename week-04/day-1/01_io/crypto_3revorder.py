# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    result = f.readlines()
    eredm = []
    for i in range(len(result)-1,-1,-1):
        eredm.append(result[i])
    f.close()
    return "".join(eredm)
