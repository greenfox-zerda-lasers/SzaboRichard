def draw_star_lines_hour_glass(num):
    star = "*"
    temp2 = num*2
    temp = 0
    for i in range(num):
        temp2-=2
        temp += 1
        # print(temp*" "+star+temp2*" "+star)
        print(temp*" "+star+(temp2+1)*" "+star)
    temp = num
    temp2 = -2
    for i in range(num):
        temp2 += 2
        temp -=1
        print((temp+1)*" "+star+" "+(temp2)*" "+star)



draw_star_lines_hour_glass(9)
print("###############################################x")

def draw_x(num):
    temp = num
    temp2 = num
    for i in range(num):
        temp -= 1
        temp2 -= 2
        print(i*" "+"*"+temp*" "+"*")

draw_x(9)
