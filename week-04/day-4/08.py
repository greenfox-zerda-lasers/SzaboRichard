# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.
def another_fun_funtc(string):
    if len(string) == 0:
        return ""
    elif string[0] == "x":
        return "" + another_fun_funtc(string[1:])
    else:
        return string[0] + another_fun_funtc(string[1:])

print(another_fun_funtc("xmaxaxmasmax"))
