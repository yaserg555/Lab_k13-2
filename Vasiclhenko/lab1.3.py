import math

#1

year = int(input('year'))
month = int(input('month'))
day = int(input('day'))
year = year % 100
print(f'{day}.{month}.{year}')

#2

x=int(input('x'))
y=int(input('y'))
a=math.tan(x+y)
v=1/a
print("{:.2e}".format(v))

#3

x=int(input('x'))
v=math.atan((1/x))
print("{:.4e}".format(v))

#4

#a=(math.log1p(10.001))*345
#a1=math.exp(a)

#b=(math.log1p(13.001))*249
#b1=math.exp(b)

#c=(math.log1p(9.001))*355
#c1=math.exp(c)

#d=(math.log1p(11.001))*269
#d1=math.exp(d)

#s=(a*b)/(c*d)
#print(s)
