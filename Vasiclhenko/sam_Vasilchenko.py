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
