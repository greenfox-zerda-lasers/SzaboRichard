# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
def yay_more_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[0] + "*" + yay_more_string(string[1:])


print(yay_more_string("XmanXX, TripleXXXX"))
