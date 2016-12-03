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
print("###############################################x")
print(" ")

def draw_x(draw_data):
    for column in range(len(draw_data)):
        for row in draw_data[column]:
            if row == 1:
                print("X")
            else:
                print(" ")

x_draw_matrix = [ [1,0,0,0,1],
                  [0,1,0,1,0],
                  [0,0,1,0,0],
                  [0,1,0,1,0],
                  [1,0,0,0,1],
                  ]
draw_x(x_draw_matrix)
