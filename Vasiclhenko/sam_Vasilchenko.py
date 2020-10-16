import math
#3

a = int(input("A"))
b = int(input("B"))
c = int(input("C"))

P=a+b+c
l=P/2
q=l*(l-a)*(l-b)*(l-c)
S=math.sqrt(q)
print(P)
print(S)

#4

x=int(input("X"))
y=int(input("Y"))
c=int(input("C"))

print(f'A[{x},{y},{c}]')


#5


a=int(input('a'))
b=int(input('b'))
c=a+b
v=math.log(c,89)
print(v)


#6


a=int(input('a'))
b=int(input('b'))
c=int(input('c'))

if (a+b==c) or (a+c==b) or (b+c==a):
    print('yes')
print('no')

#7

a=int(input('a'))
b=int(input('b'))
c=int(input('c'))
d=int(input('d'))

a1=a%2
b1=b%2
c1=c%2
d1=d%2

ma='not found'
if a1==0:
    ma=a
if b1==0 and b>ma:
    ma=b
if c1==0 and c>ma:
    ma=c
if d1==0 and d>ma:
    ma=d
print(ma)

#8

k=int(input('k'))
a=10
if k%2==0:
    k1=k/2
    while k1>1:
        a+=1
        k1+=-1
    print(a%10)
if k%2==1:
    k1=(k+1)/2
    while k1>1:
        a+=1
        k1+=-1
    print(a//10)
