from collections import Counter

def anagramm(stringA, stringB):
    a = stringA.lower().replace(" ", "")
    b = stringB.lower().replace(" ","")

    if sorted(list(a)) == sorted(list(b)):
        return True
    else:
        return False


# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

def count_letters(string):
    temp = string.lower().replace(" ","")
    cnt = Counter(list(temp))
    return cnt

# print(count_letters("afizasgzuahusuo piuodfihaspif"))
