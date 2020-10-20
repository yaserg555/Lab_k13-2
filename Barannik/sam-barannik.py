#3
a=float(input())
b=float(input())
c=float(input())
print(a+b+c)

#5
x=float(input())
y=float(input())
z=float(input())
l=[x,y,z]
print(l)

#6
from math import log
x=float(input())
y=float(input())
log(x+y, 89)

#7
a=float(input())
b=float(input())
c=float(input())
if a+b==c or a+c==b or b+c==a:
  print('Yes')

#8
k=int(input())
if k%2:
  print(((k+1)//2+9)//10)
else:
  print(((k+1)//2+9)%10)

#9  
from math import cos
i=3
while i<112:
  s=s+cos(i/(i+2))
print(s)

#11


#12
x=float(input())
y=float(input())
x=x+y
y=x-y
x=x-y
print(x','y)
