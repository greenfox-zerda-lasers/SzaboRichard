#1
print('Hello World')
a=3
a+=10
print(a)

#2
b=100
b-=7
print(b)

#3
c=44
c*=2
print(c)

#4
d=125
d/=5
print(d)

#5
e=8
e=8 ** 2
print(e)

#6
import math
f=16
print (math.sqrt(f))

#7
g1=123
g2=345
if g1>g2:
    print(g1)
else:
    print(g2)

#8
h1 = 350
h2 = 200
if (h2 **2) >h1:
    print(h2)
else:
    print(h1)

#9
i = 1357988018575474
if i % 11 == 0:
    print(i)

#10
j1 = 10
j2 = 3
if j1 > j2 // 2 and j1 < j2 **2:
    print(j1)

#11
k = 1521
# t<clear></clear>ell if k is dividable by 3 or 5
if k % 3 == 0 or k % 5 == 0:
    print(k)

#12
l = 'python'
# Tell the 2nd letter of the word
print(l[2])

#13
m = 'Apple'
temp= m
# fill the m variable with its cotnent 4 times
for n in range(3):
    m+= temp
print(m)

#14
n = 'The result is: '
a = 2
b = 3
# concat the product of a and b to the n string
n+= str(a)+" "+ str(b)
print(n)

#15
o = "pneumonoultramicroscopicsilicovolcanoconiosis"
# tell how many letters in o
print(len(o))

#16
p1 = [1, 2, 3]
p2 = [4, 5]
# tell if p2 has more elements than p1
if len(p2) > len(p1):
    print(p2)
else:
    print(p1)

#17
q = [4, 5, 6, 7]
# get the 3rd element of q
print(q[2])

#18
r = [54, 23, 66, 12]
# add the second the third
r[1]+=r[2]
print (r)

#19
s = [1, 2, 3, 8, 5, 6]
# change the 8 to 4
s[3] = 4
print (s)

#20
t = [1, 2, 3, 4, 5]
# increment the 3rd element
t[2]+= 3
print(t)

#21
u = 123
# print 'Hooray!' if the number is bigger than 100
if u > 100:
    print ('Hoory')

#22
v = 426
# print 'Yeah!' if dividable by 4 but print 'End of program' after regardless
if 426 % 4 == 0:
    print ('Yeah!')
else:
    print ('End of program')

#23
w = 24
out = 0
# if w is even increment out by one
if w % 2 == 0:
    out+=1
print (out)

#24
x = 'monkey'
# if the string is longer than 4 characters
# print 'Long!' otherwise print 'Short!'
if len(x) > 4:
    print ('Long!')
else:
    print('Short!')

#25
x = 'cheese'
# Tell if the x has even or odd number of
# characters with a True for even and
# false False output otherwise
if len(x) % 2 == 0:
    print('True')
else:
    print('False')

#26
y = 'seasons'
out = 6
# if the last and the first letter of the string
# are the same double the variable
# called out, if not half it
if y[0] == 's' and y[-1] == 's':
    out *= 2
    print (out)
else:
    out /= 2

#27
z = 13
# if z is between 10 and 20 print 'Sweet!'
# if less than 10 print 'More!',
# if more than 20 print 'Less!'
if z > 10 and  z < 20:
    if z <=10:
        print('More!')
    if z > 20:
        print('Less!')

#28
aa = [1, 2, 3]
out = 0
# if the aa list contains one element set the out to 1
# if the aa list contains two element set the out to 2
# if the aa list contains more than 2 set the out to 10
# if the aa contains no elements it should set to -1
if len(aa) == 1:
    out += 1
elif len(aa) == 2:
    out +=2
elif len(aa) > 2:
    out +=10
elif len(aa) == 0:
    out -= 1

#29
ab = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same
if credits == 50 and is_bonus != True:
    ab -= 1
elif credits < 50 and is_bonus == False:
    ab += 1
elif is_bonus == True:
    print(ab)

#30
ac = 8
time = 120
out = ''
# if ac is dividable by 4
# and time is not more than 200
# set out to 'check'
# if time is more than 200
# set out to 'Time out'
# otherwise set out to 'Run Forest Run!'
if ac % 4 == 1 and time > 200:
    out = 'check'
elif time < 200:
    out = 'Time out'
else:
    out= 'Run Forest Run!'
print (out)

#31
ad = 6
# print the numbers till ad from 0
for n in range(10):
    if n <= 6:
        print(n)

#32
ae = 4
text = 'Gold'
# print content of the text variable ae times
for n in range(ae):
    print (text)

#33
af = [4, 5, 6, 7]
# print all the elements of af
for t in af:
    print (t)

#34
ag = [3, 4, 5, 6, 7]
# please double all the elements of the list
for t in range(len(ag)):
      ag[t]*= 2
print(ag)

#35
ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end
for i in range(len(ah)):
     ah[i] += 'a'
print(ah)

#36
ah = [3, 4, 5, 6, 7]
# print the sum of all numbers in ah
summ = 0
for i in ah:
    summ += i
print(summ)

#37
# print the even numbers till 20
for i in range(21):
    if i % 2 == 0:
        print(i)
    else:
        print('hah paratlan')

#3
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101,1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

#xmas tree
# item = '*'
# 
# for i in range(11):
#     item += '*'
#     print(item)
#     for x in range(11):
#         item -= '*'
#         print(item)
