# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
def string_change(string):
    if len(string) == 0:
        return ""
    else:
        if string[0] == "x":
            return "y" + string_change(string[1:])
        else:
            return string[0] + string_change(string[1:])

print(string_change("xman"))    
