print('Алексей')
#3
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
p = a+b+c
print(f'{p}')
#4
x = int(input('x:'))
y = int(input('y:'))
print(f'{x,y}')
#6
A = int(input('A:'))
B = int(input('B:'))
C = int(input('C:'))
if A + B == C or B + C == A or A + C == B and A >= 0 and B >= 0 and C >= 0:
    print('yes')
else:
    print('no')
