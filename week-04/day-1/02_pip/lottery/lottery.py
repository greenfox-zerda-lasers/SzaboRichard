from collections import Counter
# Create a method that returns the five most frequent lottery number in a pretty table format

def five_most_frequent():
    f = open('lottery.py')
    lista = f.readlines()
    tomb = []
    topfiveL = {}
    for i in lista:
        tomb.append(i.split(';')[-5:])
        topfiveL = Counter(tomb)
    sf.close()
    return topfiveL.most_common(5)
