x=float(input())
y=float(input())
z=float(input())
from math import sqrt
print(f'периметр такого трикутникак дорівнює:{x+y+z}')
print(f'площа такого трикутникак дорівнює:{sqrt((x+y+z)/2*(x+y-z)/2*(x-y+z)/2*(-x+y+z)/2)}')


x=float(input())
y=float(input())
a=[x,y]
print(a)

#6
x=float(input())
y=float(input())
z=float(input())
if x+y==z or x+z==y or z+y==x:
    print('yes')

    #7
x=float(input())
y=float(input())
z=float(input())
k=float(input())
l=[x,y,z,k]
l.sort()
def y():
    for i in[3,2,1,0]:
        if l[i]%2 == 0:
            return l[i]
    return "not found"
print(y())

#8
k=int(input())
x=int(k/20)
y=k%20
if k%2==0:
    print((y-1)%10)
else:
    print(x+1)

    #9
from math import cos
s=0;
i=3
while i<113:
    s+=cos(i/(i+2))
    i+=2
print(s)





