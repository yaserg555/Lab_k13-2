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

x=float(input())
y=float(input())
z=float(input())
if x+y==z or x+z==y or z+y==x:
    print('yes')

